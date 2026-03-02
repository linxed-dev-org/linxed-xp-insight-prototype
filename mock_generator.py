"""
Linxed XP v4.0 — Mock Data Generator
Course-level XP blocks. Multi-subject lessons via subject_shares.
KEY: Babington courses use BABINGTON_COURSE_BLUEPRINT for real LO/Section data.
     Imaginary courses use DEMO_PROFILES fpr/assessment configs directly.
"""
import uuid, random, json, math
from datetime import datetime, timedelta
from config import (BASE_XP_RATE, PERF_DEFAULT, CATEGORIES, SUBJECT_CATEGORY_CONFIG,
    calc_lesson_subject_shares, calc_lesson_category_splits, get_multiplier_from_grade,
    calc_weighted_category_splits, DEMO_PROFILES, LESSON_DURATIONS,
    BABINGTON_COURSE_BLUEPRINT)

# ── Build Babington Blueprint Lookup ──
_BLUEPRINT_INDEX = {}
for _r in BABINGTON_COURSE_BLUEPRINT:
    _cn = _r["course"]
    if _cn not in _BLUEPRINT_INDEX:
        _BLUEPRINT_INDEX[_cn] = {"fpr_los": [], "assessment_sections": []}
    if _r["record_type"] == "fpr_lo":
        _BLUEPRINT_INDEX[_cn]["fpr_los"].append(_r)
    elif _r["record_type"] == "assessment_section":
        _BLUEPRINT_INDEX[_cn]["assessment_sections"].append(_r)

def gid(prefix=""): return f"{prefix}{uuid.uuid4().hex[:12]}"

def generate_dates(start_str, end_str, num_lessons, days=None):
    start = datetime.strptime(start_str, "%Y-%m-%d").date()
    end = datetime.strptime(end_str, "%Y-%m-%d").date()
    if not days or days == []: days = ["Saturday"]
    day_map = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    target_days = [day_map.get(d, 5) for d in days]
    all_dates = []
    cur = start
    while cur <= end:
        if cur.weekday() in target_days:
            all_dates.append(cur)
        cur += timedelta(days=1)
    if len(all_dates) >= num_lessons:
        step = max(1, len(all_dates) // num_lessons)
        selected = all_dates[::step][:num_lessons]
    else:
        selected = all_dates[:num_lessons]
    while len(selected) < num_lessons:
        selected.append(selected[-1] + timedelta(days=7) if selected else start)
    return selected[:num_lessons]


def generate_fpr_from_blueprint(course_id, student_id, blueprint_los, base_xp):
    """Generate FPR records from BABINGTON_COURSE_BLUEPRINT — real titles, skills, max_scores."""
    num_los = len(blueprint_los)
    if num_los == 0:
        return []
    xp_per_lo = round(base_xp / num_los, 6)  # F-01a

    records = []
    for bp in blueprint_los:
        skills = bp["skill_categories"]
        num_skills = bp["num_skills"]
        max_score = bp["max_score"]
        lo_idx = bp["lo_index"]
        lo_title = bp["title"]
        sub_skill_xp = round(xp_per_lo / num_skills, 6) if num_skills > 0 else xp_per_lo
        actual = random.randint(1, int(max_score))
        pct = round(actual / max_score, 6)

        for skill in skills:
            records.append({
                "lo_id": gid("lo_"),
                "course_id": course_id,
                "student_id": student_id,
                "lo_index": lo_idx,
                "lo_name": f"LO-{lo_idx}: {lo_title}",
                "skills": [skill],
                "num_skills": num_skills,
                "xp_weight": sub_skill_xp,
                "max_score": max_score,
                "actual_score": actual,
                "pct_score": pct,
                "weighted_score": round(pct * sub_skill_xp, 6),
            })
    return records


def generate_assessment_from_blueprint(course_id, student_id, blueprint_sections, base_xp):
    """Generate Assessment records from BABINGTON_COURSE_BLUEPRINT — real titles, skills, max_scores."""
    num_sections = len(blueprint_sections)
    if num_sections == 0:
        return []
    xp_per_section = round(base_xp / num_sections, 6)  # F-01b

    records = []
    for bp in blueprint_sections:
        skills = bp["skill_categories"]
        num_skills = bp["num_skills"]
        max_score = bp["max_score"]
        sec_idx = bp["section_index"]
        sec_title = bp["title"]
        sub_skill_xp = round(xp_per_section / num_skills, 6) if num_skills > 0 else xp_per_section
        actual = random.randint(0, int(max_score))
        pct = round(actual / max_score, 6) if max_score > 0 else 0

        for skill in skills:
            records.append({
                "section_id": gid("sec_"),
                "course_id": course_id,
                "student_id": student_id,
                "section_index": sec_idx,
                "section_name": sec_title,
                "skills": [skill],
                "num_skills": num_skills,
                "xp_weight": sub_skill_xp,
                "max_score": max_score,
                "actual_score": actual,
                "pct_score": pct,
                "weighted_score": round(pct * sub_skill_xp, 6),
            })
    return records


def generate_fpr_data(course_id, student_id, fpr_config, base_xp):
    """Generate FPR from DEMO_PROFILES config (imaginary courses only)."""
    los = fpr_config.get("learning_objectives", [])
    if not los: return []
    max_score = fpr_config.get("max_score", 5)
    num_los = len(los)
    xp_per_lo = round(base_xp / num_los, 6) if num_los > 0 else 0
    records = []
    for i, lo in enumerate(los):
        skills = lo.get("skills", ["Reading"])
        num_skills = len(skills)
        sub_skill_xp = round(xp_per_lo / num_skills, 6) if num_skills > 0 else xp_per_lo
        actual = random.randint(1, int(max_score))
        pct = round(actual / max_score, 6)
        for skill in skills:
            records.append({
                "lo_id": gid("lo_"), "course_id": course_id, "student_id": student_id,
                "lo_index": i + 1, "lo_name": lo.get("name", f"Learning Objective {i+1}"),
                "skills": [skill], "num_skills": num_skills, "xp_weight": sub_skill_xp,
                "max_score": max_score, "actual_score": actual, "pct_score": pct,
                "weighted_score": round(pct * sub_skill_xp, 6),
            })
    return records


def generate_assessment_data(course_id, student_id, asmt_config, base_xp):
    """Generate Assessment from DEMO_PROFILES config (imaginary courses only)."""
    sections = asmt_config.get("sections", [])
    if not sections: return []
    num_sections = len(sections)
    xp_per_section = round(base_xp / num_sections, 6) if num_sections > 0 else 0
    records = []
    for i, sec in enumerate(sections):
        skills = sec.get("skills", ["Reading"])
        num_skills = len(skills)
        max_score = sec.get("max_score", 5)
        sub_skill_xp = round(xp_per_section / num_skills, 6) if num_skills > 0 else xp_per_section
        actual = random.randint(0, int(max_score))
        pct = round(actual / max_score, 6) if max_score > 0 else 0
        for skill in skills:
            records.append({
                "section_id": gid("sec_"), "course_id": course_id, "student_id": student_id,
                "section_index": i + 1, "section_name": sec.get("name", f"Section {i+1}"),
                "skills": [skill], "num_skills": num_skills, "xp_weight": sub_skill_xp,
                "max_score": max_score, "actual_score": actual, "pct_score": pct,
                "weighted_score": round(pct * sub_skill_xp, 6),
            })
    return records


def generate_course_data(student_id, course_cfg):
    """Generate attendance + FPR/Assessment for a course.
    Babington courses → BABINGTON_COURSE_BLUEPRINT (real data).
    Imaginary courses → DEMO_PROFILES fpr/assessment configs."""
    cid = gid("crs_")
    name = course_cfg["name"]
    subj_pcts = course_cfg["subjects"]
    split_mode = course_cfg.get("split_mode", "percentage")
    grade = course_cfg.get("grade")
    dur = course_cfg.get("dur", 60)
    mult = get_multiplier_from_grade(grade) if grade else PERF_DEFAULT
    num_lessons = course_cfg.get("lessons", 30)
    days = course_cfg.get("days", ["Saturday"])
    dates = generate_dates(course_cfg["start"], course_cfg["end"], num_lessons, days)
    total_pct = sum(subj_pcts.values()) or 100
    course_shares = {s: round(p / total_pct, 6) for s, p in subj_pcts.items()}

    attendance = []
    for i, d in enumerate(dates):
        is_present = random.random() < 0.88
        mins = dur if is_present else 0
        xp_raw = round(mins * BASE_XP_RATE, 6)
        xp_adj = round(xp_raw * mult, 6)
        cat_fracs = calc_lesson_category_splits(course_shares)
        su = {cat: round(xp_adj * frac, 6) for cat, frac in cat_fracs.items()}
        attendance.append({
            "attendance_id": gid("att_"), "student_id": student_id,
            "course_id": cid, "lesson_num": i + 1,
            "att_date": d.strftime("%Y-%m-%d"),
            "att_status": "present" if is_present else "absent",
            "minutes_attended": mins, "lesson_duration": dur,
            "subjects_list": ", ".join(subj_pcts.keys()),
            "subject_shares": course_shares,
            "xp_unit_raw": xp_raw, "xp_unit_adjusted": xp_adj,
            "sub_units": su, "performance_multiplier": mult,
        })

    # ── FPR/Assessment Generation ──
    is_babington = name in _BLUEPRINT_INDEX
    base_xp = round(num_lessons * 0.6, 6)
    fpr_records, asmt_section_records = [], []

    if is_babington:
        bp = _BLUEPRINT_INDEX[name]
        if bp["fpr_los"]:
            fpr_records = generate_fpr_from_blueprint(cid, student_id, bp["fpr_los"], base_xp)
        if bp["assessment_sections"]:
            asmt_section_records = generate_assessment_from_blueprint(cid, student_id, bp["assessment_sections"], base_xp)
        has_fpr = len(bp["fpr_los"]) > 0
        has_assessment = len(bp["assessment_sections"]) > 0
    else:
        has_fpr = bool(course_cfg.get("fpr"))
        has_assessment = bool(course_cfg.get("assessment"))
        if has_fpr:
            fpr_records = generate_fpr_data(cid, student_id, course_cfg["fpr"], base_xp)
        if has_assessment:
            asmt_section_records = generate_assessment_data(cid, student_id, course_cfg["assessment"], base_xp)

    course = {
        "course_id": cid, "course_name": name, "student_id": student_id,
        "start_date": course_cfg["start"], "end_date": course_cfg["end"],
        "num_lessons": num_lessons, "lesson_duration": dur,
        "lesson_days": days, "split_mode": split_mode,
        "subject_splits": subj_pcts, "subjects_list": ", ".join(subj_pcts.keys()),
        "assessment_status": "assessed" if grade else "pending",
        "grade_pct": grade, "performance_multiplier": mult, "is_active": True,
        "has_fpr": has_fpr, "has_assessment": has_assessment,
    }

    assessment = None
    if grade:
        assessment = {
            "assessment_id": gid("asmt_"), "course_id": cid,
            "student_id": student_id, "grade_pct": grade,
            "multiplier": mult, "assessment_date": course_cfg["end"],
        }

    return {
        "course": course, "attendance": attendance, "assessment": assessment,
        "fpr_records": fpr_records, "asmt_section_records": asmt_section_records,
    }


def generate_demo_profiles():
    """Generate all demo student profiles."""
    all_data = []
    for dp in DEMO_PROFILES:
        sid = gid("stu_")
        student = {
            "student_id": sid, "student_name": dp["name"],
            "date_of_birth": dp["dob"], "enrollment_date": dp["enrollment"],
            "branch_id": dp["branch"], "status": "active",
        }
        courses, atts, asmts = [], [], []
        fpr_all, asmt_sec_all = [], []
        for cc in dp["courses"]:
            r = generate_course_data(sid, cc)
            courses.append(r["course"])
            atts.extend(r["attendance"])
            if r["assessment"]: asmts.append(r["assessment"])
            fpr_all.extend(r.get("fpr_records", []))
            asmt_sec_all.extend(r.get("asmt_section_records", []))
        all_data.append({
            "student": student, "courses": courses,
            "attendance": atts, "assessments": asmts,
            "fpr_records": fpr_all, "asmt_section_records": asmt_sec_all,
        })
    return all_data
