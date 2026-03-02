"""
Linxed XP v4.0 — Database Layer
Course-centric XP blocks. Multi-subject lessons via subject_shares JSON.
NEW: FPR (Final Progress Report) and Assessment tables for skills calculation.
"""
import sqlite3, json, os
DB_PATH = os.path.join(os.path.dirname(__file__), "linxed_xp.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH); conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON"); return conn

def init_database():
    conn = get_conn(); c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY, student_name TEXT NOT NULL,
        date_of_birth TEXT, enrollment_date TEXT NOT NULL,
        branch_id TEXT, status TEXT DEFAULT 'active')""")
    c.execute("""CREATE TABLE IF NOT EXISTS courses (
        course_id TEXT PRIMARY KEY, course_name TEXT NOT NULL,
        student_id TEXT NOT NULL, start_date TEXT, end_date TEXT,
        num_lessons INTEGER, lesson_duration INTEGER DEFAULT 60,
        lesson_days TEXT DEFAULT '[]', split_mode TEXT DEFAULT 'percentage',
        subject_splits TEXT DEFAULT '{}', subjects_list TEXT DEFAULT '',
        assessment_status TEXT DEFAULT 'pending', grade_pct REAL,
        performance_multiplier REAL DEFAULT 1.0, is_active INTEGER DEFAULT 1,
        has_fpr INTEGER DEFAULT 0, has_assessment INTEGER DEFAULT 0,
        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE)""")
    c.execute("""CREATE TABLE IF NOT EXISTS course_lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id TEXT NOT NULL, lesson_num INTEGER,
        lesson_date TEXT, subjects TEXT DEFAULT '[]',
        subject_shares TEXT DEFAULT '{}',
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE)""")
    c.execute("""CREATE TABLE IF NOT EXISTS student_attendance (
        attendance_id TEXT PRIMARY KEY, student_id TEXT NOT NULL,
        course_id TEXT NOT NULL, lesson_num INTEGER,
        att_date TEXT NOT NULL, att_status TEXT DEFAULT 'present',
        minutes_attended INTEGER DEFAULT 0, lesson_duration INTEGER DEFAULT 60,
        subjects_list TEXT DEFAULT '', subject_shares TEXT DEFAULT '{}',
        xp_unit_raw REAL DEFAULT 0, xp_unit_adjusted REAL DEFAULT 0,
        sub_units TEXT DEFAULT '{}', performance_multiplier REAL DEFAULT 1.0,
        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE)""")
    c.execute("""CREATE TABLE IF NOT EXISTS xp_assessments (
        assessment_id TEXT PRIMARY KEY, course_id TEXT NOT NULL,
        student_id TEXT, grade_pct REAL, multiplier REAL DEFAULT 1.0,
        assessment_date TEXT,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE)""")
    # NEW: FPR Learning Objectives — skill-rows for Final Progress Report
    c.execute("""CREATE TABLE IF NOT EXISTS fpr_learning_objectives (
        lo_id TEXT PRIMARY KEY,
        course_id TEXT NOT NULL,
        student_id TEXT NOT NULL,
        lo_index INTEGER,
        lo_name TEXT,
        skills TEXT DEFAULT '[]',
        num_skills INTEGER DEFAULT 1,
        xp_weight REAL DEFAULT 0,
        max_score REAL DEFAULT 5,
        actual_score REAL DEFAULT 0,
        pct_score REAL DEFAULT 0,
        weighted_score REAL DEFAULT 0,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE)""")
    # NEW: Assessment Sections — skill-rows for Assessment
    c.execute("""CREATE TABLE IF NOT EXISTS assessment_sections (
        section_id TEXT PRIMARY KEY,
        course_id TEXT NOT NULL,
        student_id TEXT NOT NULL,
        section_index INTEGER,
        section_name TEXT,
        skills TEXT DEFAULT '[]',
        num_skills INTEGER DEFAULT 1,
        xp_weight REAL DEFAULT 0,
        max_score REAL DEFAULT 5,
        actual_score REAL DEFAULT 0,
        pct_score REAL DEFAULT 0,
        weighted_score REAL DEFAULT 0,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE)""")
    conn.commit(); conn.close()

def save_student(s):
    conn = get_conn()
    conn.execute("INSERT OR REPLACE INTO students VALUES (?,?,?,?,?,?)",
        (s["student_id"],s["student_name"],s.get("date_of_birth",""),s["enrollment_date"],s.get("branch_id",""),s.get("status","active")))
    conn.commit(); conn.close()

def get_student(sid):
    conn = get_conn(); r = conn.execute("SELECT * FROM students WHERE student_id=?",(sid,)).fetchone()
    conn.close(); return dict(r) if r else None

def get_all_student_profiles():
    conn = get_conn()
    rows = conn.execute("""SELECT s.*, COUNT(DISTINCT c.course_id) as course_count,
        GROUP_CONCAT(DISTINCT c.course_name) as courses_list
        FROM students s LEFT JOIN courses c ON s.student_id=c.student_id
        GROUP BY s.student_id ORDER BY s.student_name""").fetchall()
    conn.close(); return [dict(r) for r in rows]

def delete_student(sid):
    conn = get_conn()
    conn.execute("DELETE FROM fpr_learning_objectives WHERE student_id=?",(sid,))
    conn.execute("DELETE FROM assessment_sections WHERE student_id=?",(sid,))
    conn.execute("DELETE FROM student_attendance WHERE student_id=?",(sid,))
    conn.execute("DELETE FROM xp_assessments WHERE student_id=?",(sid,))
    for c in conn.execute("SELECT course_id FROM courses WHERE student_id=?",(sid,)).fetchall():
        conn.execute("DELETE FROM course_lessons WHERE course_id=?",(c["course_id"],))
    conn.execute("DELETE FROM courses WHERE student_id=?",(sid,))
    conn.execute("DELETE FROM students WHERE student_id=?",(sid,))
    conn.commit(); conn.close()

def save_course(c):
    conn = get_conn()
    ss = c.get("subject_splits",{}); sl = c.get("subjects_list",""); ld = c.get("lesson_days",[])
    if isinstance(ss,dict): ss=json.dumps(ss)
    if isinstance(ld,list): ld=json.dumps(ld)
    conn.execute("""INSERT OR REPLACE INTO courses VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (c["course_id"],c["course_name"],c["student_id"],c.get("start_date"),c.get("end_date"),
         c.get("num_lessons"),c.get("lesson_duration",60),ld,c.get("split_mode","percentage"),
         ss,sl,c.get("assessment_status","pending"),c.get("grade_pct"),
         c.get("performance_multiplier",1.0),int(c.get("is_active",True)),
         int(c.get("has_fpr",False)),int(c.get("has_assessment",False))))
    conn.commit(); conn.close()

def get_student_courses(sid):
    conn = get_conn()
    rows = conn.execute("SELECT * FROM courses WHERE student_id=? ORDER BY start_date",(sid,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        for f in ["subject_splits","lesson_days"]:
            if isinstance(d.get(f),str):
                try: d[f]=json.loads(d[f])
                except: pass
        result.append(d)
    return result

def delete_course(cid):
    conn = get_conn()
    conn.execute("DELETE FROM fpr_learning_objectives WHERE course_id=?",(cid,))
    conn.execute("DELETE FROM assessment_sections WHERE course_id=?",(cid,))
    conn.execute("DELETE FROM student_attendance WHERE course_id=?",(cid,))
    conn.execute("DELETE FROM xp_assessments WHERE course_id=?",(cid,))
    conn.execute("DELETE FROM course_lessons WHERE course_id=?",(cid,))
    conn.execute("DELETE FROM courses WHERE course_id=?",(cid,))
    conn.commit(); conn.close()

def save_attendance_batch(records):
    conn = get_conn()
    for r in records:
        su = r.get("sub_units",{}); ss = r.get("subject_shares",{})
        if isinstance(su,dict): su=json.dumps(su)
        if isinstance(ss,dict): ss=json.dumps(ss)
        conn.execute("""INSERT OR REPLACE INTO student_attendance VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (r["attendance_id"],r["student_id"],r["course_id"],r.get("lesson_num",0),
             r["att_date"],r.get("att_status","present"),r.get("minutes_attended",0),
             r.get("lesson_duration",60),r.get("subjects_list",""),ss,
             r.get("xp_unit_raw",0),r.get("xp_unit_adjusted",0),su,
             r.get("performance_multiplier",1.0)))
    conn.commit(); conn.close()

def get_student_attendance(sid):
    conn = get_conn()
    rows = conn.execute("""SELECT a.*,c.course_name FROM student_attendance a
        LEFT JOIN courses c ON a.course_id=c.course_id
        WHERE a.student_id=? ORDER BY a.att_date""",(sid,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        for f in ["sub_units","subject_shares"]:
            if isinstance(d.get(f),str):
                try: d[f]=json.loads(d[f])
                except: d[f]={}
        result.append(d)
    return result

def save_assessment(a):
    conn = get_conn()
    conn.execute("INSERT OR REPLACE INTO xp_assessments VALUES (?,?,?,?,?,?)",
        (a["assessment_id"],a["course_id"],a.get("student_id",""),
         a.get("grade_pct"),a.get("multiplier",1.0),a.get("assessment_date","")))
    conn.commit(); conn.close()

def get_student_assessments(sid):
    conn = get_conn()
    rows = conn.execute("SELECT * FROM xp_assessments WHERE student_id=?",(sid,)).fetchall()
    conn.close(); return [dict(r) for r in rows]

# ── NEW: FPR Learning Objectives ──
def save_fpr_lo(lo):
    conn = get_conn()
    skills = lo.get("skills", [])
    if isinstance(skills, list): skills = json.dumps(skills)
    conn.execute("""INSERT OR REPLACE INTO fpr_learning_objectives VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
        (lo["lo_id"], lo["course_id"], lo["student_id"], lo.get("lo_index",0),
         lo.get("lo_name",""), skills, lo.get("num_skills",1),
         lo.get("xp_weight",0), lo.get("max_score",5),
         lo.get("actual_score",0), lo.get("pct_score",0), lo.get("weighted_score",0)))
    conn.commit(); conn.close()

def save_fpr_lo_batch(records):
    conn = get_conn()
    for lo in records:
        skills = lo.get("skills", [])
        if isinstance(skills, list): skills = json.dumps(skills)
        conn.execute("""INSERT OR REPLACE INTO fpr_learning_objectives VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (lo["lo_id"], lo["course_id"], lo["student_id"], lo.get("lo_index",0),
             lo.get("lo_name",""), skills, lo.get("num_skills",1),
             lo.get("xp_weight",0), lo.get("max_score",5),
             lo.get("actual_score",0), lo.get("pct_score",0), lo.get("weighted_score",0)))
    conn.commit(); conn.close()

def get_course_fpr_los(course_id):
    conn = get_conn()
    rows = conn.execute("SELECT * FROM fpr_learning_objectives WHERE course_id=? ORDER BY lo_index",(course_id,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        if isinstance(d.get("skills"), str):
            try: d["skills"] = json.loads(d["skills"])
            except: d["skills"] = []
        result.append(d)
    return result

def get_student_all_fpr_los(sid):
    conn = get_conn()
    rows = conn.execute("""SELECT f.*, c.course_name FROM fpr_learning_objectives f
        LEFT JOIN courses c ON f.course_id=c.course_id
        WHERE f.student_id=? ORDER BY c.start_date, f.lo_index""",(sid,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        if isinstance(d.get("skills"), str):
            try: d["skills"] = json.loads(d["skills"])
            except: d["skills"] = []
        result.append(d)
    return result

# ── NEW: Assessment Sections ──
def save_assessment_section(sec):
    conn = get_conn()
    skills = sec.get("skills", [])
    if isinstance(skills, list): skills = json.dumps(skills)
    conn.execute("""INSERT OR REPLACE INTO assessment_sections VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
        (sec["section_id"], sec["course_id"], sec["student_id"], sec.get("section_index",0),
         sec.get("section_name",""), skills, sec.get("num_skills",1),
         sec.get("xp_weight",0), sec.get("max_score",5),
         sec.get("actual_score",0), sec.get("pct_score",0), sec.get("weighted_score",0)))
    conn.commit(); conn.close()

def save_assessment_section_batch(records):
    conn = get_conn()
    for sec in records:
        skills = sec.get("skills", [])
        if isinstance(skills, list): skills = json.dumps(skills)
        conn.execute("""INSERT OR REPLACE INTO assessment_sections VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (sec["section_id"], sec["course_id"], sec["student_id"], sec.get("section_index",0),
             sec.get("section_name",""), skills, sec.get("num_skills",1),
             sec.get("xp_weight",0), sec.get("max_score",5),
             sec.get("actual_score",0), sec.get("pct_score",0), sec.get("weighted_score",0)))
    conn.commit(); conn.close()

def get_course_assessment_sections(course_id):
    conn = get_conn()
    rows = conn.execute("SELECT * FROM assessment_sections WHERE course_id=? ORDER BY section_index",(course_id,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        if isinstance(d.get("skills"), str):
            try: d["skills"] = json.loads(d["skills"])
            except: d["skills"] = []
        result.append(d)
    return result

def get_student_all_assessment_sections(sid):
    conn = get_conn()
    rows = conn.execute("""SELECT a.*, c.course_name FROM assessment_sections a
        LEFT JOIN courses c ON a.course_id=c.course_id
        WHERE a.student_id=? ORDER BY c.start_date, a.section_index""",(sid,)).fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        if isinstance(d.get("skills"), str):
            try: d["skills"] = json.loads(d["skills"])
            except: d["skills"] = []
        result.append(d)
    return result
