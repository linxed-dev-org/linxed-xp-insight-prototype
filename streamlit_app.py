"""Linxed XP Framework v4.0 — 25 Feb FPR/Assessment Calculation Framework Added"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import json, math
from datetime import datetime, date, timedelta
from collections import defaultdict
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from config import *
from database import *
from mock_generator import gid, generate_dates, generate_course_data, generate_demo_profiles, generate_fpr_data, generate_assessment_data
from xp_engine import XPCalculationEngine
from skills_engine import compute_full_skills_pipeline
from theme import get_premium_css, metric_card, progress_bar, badge_html

st.set_page_config(page_title="Linxed XP Framework", page_icon="", layout="wide", initial_sidebar_state="expanded")
st.markdown(get_premium_css(), unsafe_allow_html=True)
st.markdown("""<style>
header[data-testid="stHeader"]{background:transparent!important;height:0!important;min-height:0!important}
div[data-testid="stToolbar"],div[data-testid="stDecoration"],.stDeployButton,#MainMenu,footer{display:none!important}
.metric-value{font-size:28px!important}.metric-label{font-size:14px!important}
.skill-capsule{display:inline-block;padding:5px 14px;border-radius:20px;font-size:13px;font-weight:600;margin:3px;
background:rgba(78,168,255,0.12);color:#4ea8ff;border:1px solid rgba(78,168,255,0.25)}
.glass-card-skill{background:rgba(20,30,55,0.6);backdrop-filter:blur(14px);border:1px solid rgba(100,160,255,0.15);
border-radius:14px;padding:20px;margin-bottom:14px;box-shadow:0 0 25px rgba(78,168,255,0.08)}
.score-pill{display:inline-block;padding:4px 12px;border-radius:10px;font-size:14px;font-weight:700}
.score-high{background:rgba(52,211,153,0.15);color:#34d399}
.score-mid{background:rgba(251,191,36,0.15);color:#fbbf24}
.score-low{background:rgba(248,113,113,0.15);color:#f87171}
.white-card{background:#ffffff;border-radius:16px;padding:28px;margin-bottom:16px;box-shadow:0 2px 16px rgba(0,0,0,0.06);color:#1a1a2e}
.fpr-grade-box{display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:12px;font-size:22px;font-weight:800}
</style>""", unsafe_allow_html=True)
init_database()

# Auto-generate demo profiles on first launch
if not get_all_student_profiles():
    demos = generate_demo_profiles()
    for dp in demos:
        save_student(dp["student"])
        for c in dp["courses"]: save_course(c)
        if dp["attendance"]: save_attendance_batch(dp["attendance"])
        for a in dp["assessments"]: save_assessment(a)
        if dp.get("fpr_records"): save_fpr_lo_batch(dp["fpr_records"])
        if dp.get("asmt_section_records"): save_assessment_section_batch(dp["asmt_section_records"])

# ── Chart defaults — WHITE readable text for premium dark theme
_PLT_BASE = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter", color="#e2e8f0", size=14),
    margin=dict(l=40, r=20, t=50, b=40),
    hoverlabel=dict(bgcolor="#1a2340", font_size=14, font_color="#f1f5f9"),
    legend=dict(font=dict(color="#e2e8f0", size=13)))
_AXIS_X = dict(gridcolor="rgba(100,160,255,0.08)", tickfont=dict(color="#cbd5e1", size=13))
_AXIS_Y = dict(gridcolor="rgba(100,160,255,0.08)", tickfont=dict(color="#cbd5e1", size=13))

def _plt(**overrides):
    """Build plotly layout dict, merging axis overrides properly."""
    layout = {**_PLT_BASE}
    xa = {**_AXIS_X, **overrides.pop("xaxis", {})}
    ya = {**_AXIS_Y, **overrides.pop("yaxis", {})}
    layout["xaxis"] = xa
    layout["yaxis"] = ya
    layout.update(overrides)
    return layout
PAL = ["#818cf8", "#2dd4bf", "#fbbf24", "#c084fc", "#fb7185", "#38bdf8", "#e879f9", "#34d399"]
CC = {"Academic": "#60a5fa", "Health_Fitness": "#34d399", "Music": "#a78bfa",
      "Games_Strategy": "#f59e0b", "Arts_Creative": "#f472b6", "Social": "#22d3ee"}

if "page" not in st.session_state: st.session_state.page = "mock_data"
if "selected_student" not in st.session_state: st.session_state.selected_student = None
def set_page(p): st.session_state.page = p

def _build_engine(sid):
    s = get_student(sid)
    if not s: return None
    courses = get_student_courses(sid); att = get_student_attendance(sid); asmts = get_student_assessments(sid)
    if not att: return None
    blocks = [{"block_id": c["course_id"], "student_id": sid, "course_id": c["course_id"],
               "course_name": c["course_name"], "block_name": c["course_name"],
               "is_active": c.get("is_active", 1), "performance_multiplier": c.get("performance_multiplier", 1.0),
               "assessment_status": c.get("assessment_status", "pending"), "grade_pct": c.get("grade_pct")} for c in courses]
    for a in att: a["block_id"] = a["course_id"]
    eng = XPCalculationEngine(s, blocks, att, asmts)
    do = st.session_state.get("decay_overrides")
    if do: eng.decay_overrides = do
    return eng.compute_all()

def _build_skills(sid):
    courses = get_student_courses(sid)
    fpr_los = get_student_all_fpr_los(sid)
    asmt_secs = get_student_all_assessment_sections(sid)
    if not fpr_los and not asmt_secs: return None
    return compute_full_skills_pipeline(fpr_los, asmt_secs, courses)

def _score_class(pct):
    if pct >= 0.7: return "score-high"
    if pct >= 0.4: return "score-mid"
    return "score-low"

def _get_skills_for_subjects(selected_subjs):
    """Get available skills based on selected subjects — for FPR/Assessment skill selection.
    Skills come ONLY from SUBJECT_SKILLS for the selected subjects. No hardcoded fallback."""
    skills = set()
    for subj in selected_subjs:
        subj_skills = SUBJECT_SKILLS.get(subj, [])
        if subj_skills:
            skills.update(subj_skills)
    # If somehow no skills found (shouldn't happen now), provide generic fallback
    if not skills:
        skills = {"Skill 1", "Skill 2", "Skill 3"}
    return sorted(skills)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown('<div class="brand-header"><div class="brand-name">Linxed</div><div class="brand-subtitle">XP Framework v4.0</div></div>', unsafe_allow_html=True)
    for key, label in [("mock_data", "Student Profile Builder"), ("data_dashboard", "Data Dashboard"),
                       ("calculations", "Calculation Pipeline"), ("skills_calc", "Skills Calculation"),
                       ("xp_dashboard", "XP Overview"), ("insights", "Insights & Charts"),
                       ("final_report", "Final Report"), ("formulas", "Formulas"), ("glossary", "Glossary")]:
        st.button(label, key=f"nav_{key}", on_click=set_page, args=(key,),
                  type="primary" if st.session_state.page == key else "secondary", use_container_width=True)
    profiles = get_all_student_profiles()
    if profiles:
        st.markdown("---")
        st.markdown('<div style="font-size:12px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px">Active Profiles</div>', unsafe_allow_html=True)
        opts = {p["student_id"]: f"{p['student_name']} ({p['course_count'] or 0}c)" for p in profiles}
        sel = st.selectbox("Select", list(opts.keys()), format_func=lambda x: opts[x], key="sb_sel", label_visibility="collapsed")
        if sel: st.session_state.selected_student = sel
    st.markdown("---")
    if st.checkbox("Decay Override", key="dt"):
        da = [st.number_input(f"{b['label']} A", 0.0, 1.0, b["rate"], 0.00001, format="%.5f", key=f"da{i}") for i, b in enumerate(DECAY_RATES_ACTIVE)]
        di = [st.number_input(f"{b['label']} I", 0.0, 1.0, b["rate"], 0.00001, format="%.5f", key=f"di{i}") for i, b in enumerate(DECAY_RATES_INACTIVE)]
        st.session_state["decay_overrides"] = {
            "active": [{"min_months": b["min_months"], "max_months": b["max_months"], "rate": da[i]} for i, b in enumerate(DECAY_RATES_ACTIVE)],
            "inactive": [{"min_months": b["min_months"], "max_months": b["max_months"], "rate": di[i]} for i, b in enumerate(DECAY_RATES_INACTIVE)]}
    else:
        st.session_state.pop("decay_overrides", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# STUDENT PROFILE BUILDER — Steps 1-7 with live category splits
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_mock_data():
    st.markdown('<div class="page-title">Student Profile Builder</div><div class="page-subtitle">Course Creation with Final Progress Report & Assessment</div>', unsafe_allow_html=True)
    profiles = get_all_student_profiles()
    if profiles:
        st.markdown('<div class="section-title">Existing Profiles</div>', unsafe_allow_html=True)
        for ri in range(0, len(profiles), 2):
            cols = st.columns(2)
            for ci, p in enumerate(profiles[ri:ri+2]):
                with cols[ci]:
                    courses = get_student_courses(p["student_id"])
                    fpr_count = len(get_student_all_fpr_los(p["student_id"]))
                    asmt_count = len(get_student_all_assessment_sections(p["student_id"]))
                    clines = "".join(f'<div style="font-size:14px;color:var(--accent-cyan);margin-top:2px">{c["course_name"]} | {c.get("subjects_list","")}</div>' for c in courses)
                    fpr_badge = f' <span class="skill-capsule" style="font-size:11px">{fpr_count} LOs</span>' if fpr_count else ""
                    asmt_badge = f' <span class="skill-capsule" style="font-size:11px;background:rgba(251,191,36,0.12);color:#fbbf24;border-color:rgba(251,191,36,0.25)">{asmt_count} Sections</span>' if asmt_count else ""
                    st.markdown(f'<div class="glass-card-sm" style="padding:16px;min-height:100px"><div style="font-size:18px;font-weight:700;color:var(--text-primary)">{p["student_name"]}{fpr_badge}{asmt_badge}</div><div style="font-size:14px;color:var(--text-secondary)">{len(courses)} courses | Enrolled: {(p.get("enrollment_date",""))[:10]}</div>{clines}</div>', unsafe_allow_html=True)
                    if st.button("Delete", key=f"del_{p['student_id']}", type="secondary"):
                        delete_student(p["student_id"])
                        if st.session_state.selected_student == p["student_id"]: st.session_state.selected_student = None
                        st.rerun()

    st.markdown("---")
    st.markdown('<div class="section-title">Create New Student Profile</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        sn = st.text_input("Full Name", "", key="sn")
        ed = st.date_input("Enrollment Date", date(2025, 9, 1), key="ed")
    with c2:
        dob = st.date_input("Date of Birth", date(2015, 3, 15), key="dob")
        br = st.selectbox("Branch", [b["name"] for b in BRANCHES], key="br")
    nc = st.number_input("Number of Courses", 1, 8, 2, key="nc")
    all_subjs = sorted(SUBJECT_CATEGORY_CONFIG.keys())

    all_courses_cfg = []
    for ci in range(int(nc)):
        st.markdown(f'---\n### Course {ci+1}')
        # Step 1: Name
        cname = st.text_input("Step 1 — Course Name", key=f"cn_{ci}")
        # Step 2: Schedule
        st.markdown("**Step 2 — Course Schedule**")
        s2a, s2b, s2c = st.columns(3)
        with s2a:
            cstart = st.date_input("Start Date", date(2025, 9, 1), key=f"cs_{ci}")
            cend = st.date_input("End Date", date.today(), key=f"ce_{ci}")
        with s2b:
            nles = st.number_input("Number of Lessons", 5, 200, 30, key=f"nl_{ci}")
            cdur = st.selectbox("Lesson Duration (min)", LESSON_DURATIONS, index=2, key=f"cd_{ci}")
        with s2c:
            cdays = st.multiselect("Lesson Days", DAYS_OF_WEEK, default=["Saturday"], key=f"cdy_{ci}")
            casmt = st.radio("Assessment", ["Pending", "Enter Grade (%)"], key=f"ca_{ci}", horizontal=True)
        cgrade = None
        if "Enter" in casmt:
            cgrade = st.slider("Grade %", 0, 100, 80, key=f"cg_{ci}")
            m = get_multiplier_from_grade(cgrade)
            st.markdown(f"<span style='color:var(--accent-green);font-size:15px'>Grade: {cgrade}% → Multiplier: {m}x</span>", unsafe_allow_html=True)

        # Step 3: Subjects
        st.markdown("**Step 3 — Course Subjects**")
        nsub = st.number_input("Number of Subjects", 1, 10, 3, key=f"ns_{ci}")
        selected_subjs = [st.selectbox(f"Subject {j+1}", all_subjs, key=f"ss_{ci}_{j}") for j in range(int(nsub))]

        # Step 4: Split Mode with LIVE weighted category splits
        split_mode = st.selectbox("**Step 4 — Subject Split Method**",
            ["Percentage Split (define % per subject)", "Lesson Split (assign subjects per lesson)"], key=f"sm_{ci}")
        is_pct = "Percentage" in split_mode
        subj_pcts = {}
        lesson_assignments = []

        if is_pct:
            st.markdown("**Define subject percentage splits** (must sum to 100):")
            scols = st.columns(min(len(selected_subjs), 4))
            for j, subj in enumerate(selected_subjs):
                with scols[j % len(scols)]:
                    subj_pcts[subj] = st.number_input(subj, 0.0, 100.0, round(100/len(selected_subjs), 1), key=f"sp_{ci}_{j}")
            # LIVE Weighted Category Splits
            wc = calc_weighted_category_splits(subj_pcts)
            active_wc = {CATEGORY_DISPLAY.get(c, c): f"{v:.1f}%" for c, v in wc.items() if v > 0}
            st.markdown(f"**Weighted Category Splits:** {' | '.join(f'{k}: {v}' for k, v in active_wc.items())}")
        else:
            st.markdown("**Assign subjects to each lesson:**")
            dates = generate_dates(cstart.strftime("%Y-%m-%d"), cend.strftime("%Y-%m-%d"), int(nles), cdays)
            for li in range(int(nles)):
                lc1, lc2, lc3 = st.columns([1, 2, 4])
                with lc1:
                    st.markdown(f"<div style='padding:6px;font-size:14px;color:var(--text-muted)'>L{li+1}</div>", unsafe_allow_html=True)
                with lc2:
                    st.markdown(f"<div style='padding:6px;font-size:14px;color:var(--text-secondary)'>{dates[li].strftime('%Y-%m-%d') if li < len(dates) else ''}</div>", unsafe_allow_html=True)
                with lc3:
                    ls = st.multiselect("Subjects", selected_subjs, default=[selected_subjs[li % len(selected_subjs)]], key=f"la_{ci}_{li}", label_visibility="collapsed")
                    lesson_assignments.append(ls if ls else [selected_subjs[0]])
            # Calculate subject splits from lesson assignments
            subj_counts = defaultdict(float)
            for la in lesson_assignments:
                share = 1.0 / len(la) if la else 0
                for s in la: subj_counts[s] += share
            total_c = sum(subj_counts.values()) or 1
            subj_pcts = {s: round(c/total_c*100, 1) for s, c in subj_counts.items()}
            # LIVE Calculated Subject Splits
            st.markdown(f"**Calculated Subject Splits:** {' | '.join(f'{s}: {p}%' for s, p in subj_pcts.items())}")
            # LIVE Weighted Category Splits
            wc = calc_weighted_category_splits(subj_pcts)
            active_wc = {CATEGORY_DISPLAY.get(c, c): f"{v:.1f}%" for c, v in wc.items() if v > 0}
            st.markdown(f"**Weighted Category Splits:** {' | '.join(f'{k}: {v}' for k, v in active_wc.items())}")

        # Step 5: FPR & Assessment
        st.markdown("**Step 5 — Final Progress Report & Assessment**")
        fpr_option = st.selectbox("Course Reporting Type",
            ["No FPR/Assessment", "Final Progress Report Only", "Final Progress Report + Assessment"], key=f"fpr_opt_{ci}")
        fpr_config = None
        asmt_config = None
        # Get skills for selected subjects
        available_skills = _get_skills_for_subjects(selected_subjs)

        if fpr_option != "No FPR/Assessment":
            st.markdown("**Step 6 — Define Learning Objectives**")
            n_los = st.number_input("Number of Learning Objectives", 1, 30, 4, key=f"nlo_{ci}")
            los_list = []
            for li in range(int(n_los)):
                lc1, lc2, lc3 = st.columns([3, 3, 2])
                with lc1:
                    lo_name = st.text_input(f"LO-{li+1} Name", f"Learning Objective {li+1}", key=f"lon_{ci}_{li}")
                with lc2:
                    lo_skills = st.multiselect(f"Skills (from subjects)", available_skills,
                        default=[available_skills[li % len(available_skills)]] if available_skills else [],
                        key=f"losk_{ci}_{li}")
                with lc3:
                    st.markdown(f"<div style='padding:28px 0 0 0;font-size:13px;color:var(--text-muted)'>Max: 5 | Skills: {len(lo_skills)}</div>", unsafe_allow_html=True)
                los_list.append({"name": lo_name, "skills": lo_skills if lo_skills else ["Reading"]})
            fpr_config = {"learning_objectives": los_list, "max_score": 5}

            if "Assessment" in fpr_option:
                st.markdown("**Step 7 — Define Assessment Sections**")
                n_secs = st.number_input("Number of Sections", 1, 20, 3, key=f"nsec_{ci}")
                secs_list = []
                for si in range(int(n_secs)):
                    sc1, sc2, sc3 = st.columns([3, 2, 2])
                    with sc1:
                        sec_name = st.text_input(f"Section {si+1}", f"Section {si+1}", key=f"secn_{ci}_{si}")
                    with sc2:
                        sec_skills = st.multiselect(f"Skills (from subjects)", available_skills,
                            default=[available_skills[si % len(available_skills)]] if available_skills else [],
                            key=f"secsk_{ci}_{si}")
                    with sc3:
                        sec_max = st.number_input(f"Max Score", 1, 100, 20 if si == 0 else 5, key=f"secmax_{ci}_{si}")
                    secs_list.append({"name": sec_name, "skills": sec_skills if sec_skills else ["Reading"], "max_score": sec_max})
                asmt_config = {"sections": secs_list}

        all_courses_cfg.append({
            "name": cname or f"Course {ci+1}", "start": cstart.strftime("%Y-%m-%d"), "end": cend.strftime("%Y-%m-%d"),
            "lessons": int(nles), "days": cdays, "dur": cdur, "split_mode": "percentage" if is_pct else "lesson",
            "subjects": subj_pcts, "grade": cgrade, "lesson_assignments": lesson_assignments if not is_pct else None,
            "fpr": fpr_config, "assessment": asmt_config})

    # ── ENROLLMENT SUMMARY TABLE 1: Course Overview (matching v3 columns)
    if all_courses_cfg:
        st.markdown('<div class="section-title">Enrollment Summary — Courses</div>', unsafe_allow_html=True)
        rows = []
        for cc in all_courses_cfg:
            wc2 = calc_weighted_category_splits(cc["subjects"])
            active_cats = " | ".join(f'{CATEGORY_DISPLAY.get(c,c)[:5]}: {v:.0f}%' for c, v in wc2.items() if v > 0)
            rows.append({
                "Course": cc["name"],
                "Subjects": ", ".join(cc["subjects"].keys()),
                "Lessons": cc["lessons"],
                "Duration": f"{cc['dur']}min",
                "Period": f'{cc["start"]} to {cc["end"]}',
                "Assessment": f'{cc["grade"]}%' if cc["grade"] else "Pending",
                "Split Type": "% Split" if cc["split_mode"] == "percentage" else "Lesson Split",
                "Subject Splits": " | ".join(f'{s}:{p:.0f}%' for s, p in cc["subjects"].items()),
                "Category Splits": active_cats,
            })
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

        # ── ENROLLMENT SUMMARY TABLE 2: FPR/Assessment Overview
        fpr_rows = []
        for cc in all_courses_cfg:
            has_fpr = bool(cc.get("fpr"))
            has_asmt = bool(cc.get("assessment"))
            if has_fpr or has_asmt:
                rtype = "FPR + Assessment" if has_fpr and has_asmt else "FPR Only" if has_fpr else "No FPR/Assessment"
                n_los = len(cc["fpr"]["learning_objectives"]) if has_fpr else 0
                n_secs = len(cc["assessment"]["sections"]) if has_asmt else 0
                all_skills_set = set()
                if has_fpr:
                    for lo in cc["fpr"]["learning_objectives"]:
                        all_skills_set.update(lo.get("skills", []))
                if has_asmt:
                    for sec in cc["assessment"]["sections"]:
                        all_skills_set.update(sec.get("skills", []))
                fpr_rows.append({
                    "Course": cc["name"],
                    "Reporting Type": rtype,
                    "Learning Objectives": n_los,
                    "Assessment Sections": n_secs,
                    "Associated Skills": ", ".join(sorted(all_skills_set)),
                })
            else:
                fpr_rows.append({"Course": cc["name"], "Reporting Type": "No FPR/Assessment",
                    "Learning Objectives": 0, "Assessment Sections": 0, "Associated Skills": "—"})
        if fpr_rows:
            st.markdown('<div class="section-title">Enrollment Summary — FPR & Assessment</div>', unsafe_allow_html=True)
            st.dataframe(pd.DataFrame(fpr_rows), use_container_width=True, hide_index=True)

    if st.button("Generate & Save Student Profile", type="primary", use_container_width=True):
        if not sn.strip():
            st.error("Enter student name.")
            return
        sid = gid("stu_")
        student = {"student_id": sid, "student_name": sn.strip(), "date_of_birth": dob.strftime("%Y-%m-%d"),
                   "enrollment_date": ed.strftime("%Y-%m-%d"),
                   "branch_id": next((b["id"] for b in BRANCHES if b["name"] == br), BRANCHES[0]["id"]), "status": "active"}
        save_student(student)
        total_att = 0
        for cc in all_courses_cfg:
            r = generate_course_data(sid, cc)
            save_course(r["course"])
            if r["attendance"]: save_attendance_batch(r["attendance"]); total_att += len(r["attendance"])
            if r["assessment"]: save_assessment(r["assessment"])
            if r.get("fpr_records"): save_fpr_lo_batch(r["fpr_records"])
            if r.get("asmt_section_records"): save_assessment_section_batch(r["asmt_section_records"])
        st.session_state.selected_student = sid
        st.success(f"Created: {sn.strip()} — {len(all_courses_cfg)} courses, {total_att} attendance records.")
        st.rerun()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DATA DASHBOARD — with total hours, unique subjects, FPR/Assessment counts
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_data_dashboard():
    st.markdown('<div class="page-title">Data Dashboard</div><div class="page-subtitle">Course & subject data overview</div>', unsafe_allow_html=True)
    sid = st.session_state.selected_student
    if not sid: st.info("Select a student from the sidebar."); return
    s = get_student(sid); courses = get_student_courses(sid); att = get_student_attendance(sid)
    if not s: return
    present = [a for a in att if a["att_status"] == "present"]
    total_m = sum(a["minutes_attended"] for a in present)
    # Count unique subjects across all attendance
    sset = set()
    for a in present:
        sh = a.get("subject_shares", {})
        if isinstance(sh, str):
            try: sh = json.loads(sh)
            except: sh = {}
        sset.update(sh.keys())
    # Count FPR and Assessment
    fpr_all = get_student_all_fpr_los(sid)
    asmt_all = get_student_all_assessment_sections(sid)
    fpr_course_count = len(set(r["course_id"] for r in fpr_all)) if fpr_all else 0
    asmt_course_count = len(set(r["course_id"] for r in asmt_all)) if asmt_all else 0
    # Unique skills
    all_skills_set = set()
    for r in fpr_all:
        sk = r.get("skills", [])
        if isinstance(sk, str):
            try: sk = json.loads(sk)
            except: sk = []
        all_skills_set.update(sk)
    for r in asmt_all:
        sk = r.get("skills", [])
        if isinstance(sk, str):
            try: sk = json.loads(sk)
            except: sk = []
        all_skills_set.update(sk)

    # ROW 1: Core metrics
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(metric_card(len(courses), "Courses"), unsafe_allow_html=True)
    with c2: st.markdown(metric_card(len(present), "Present Sessions", "metric-green"), unsafe_allow_html=True)
    with c3: st.markdown(metric_card(f"{round(total_m/60,1)}h", "Total Hours", "metric-orange"), unsafe_allow_html=True)
    with c4: st.markdown(metric_card(len(sset), "Unique Subjects", "metric-purple"), unsafe_allow_html=True)
    # ROW 2: Skills & FPR/Assessment metrics
    c5, c6, c7, c8 = st.columns(4)
    with c5: st.markdown(metric_card(len(all_skills_set), "Unique Skills", "metric-cyan"), unsafe_allow_html=True)
    with c6: st.markdown(metric_card(fpr_course_count, "Courses with FPR", "metric-green"), unsafe_allow_html=True)
    with c7: st.markdown(metric_card(asmt_course_count, "Courses with Assessment", "metric-gold"), unsafe_allow_html=True)
    with c8: st.markdown(metric_card(f"{len(fpr_all)}+{len(asmt_all)}", "Skill-Rows (LO+Sec)", "metric-purple"), unsafe_allow_html=True)

    # Course Details
    st.markdown('<div class="section-title">Course Details</div>', unsafe_allow_html=True)
    for c in courses:
        cp = [a for a in present if a["course_id"] == c["course_id"]]
        cm = sum(a["minutes_attended"] for a in cp)
        ss = c.get("subject_splits", {})
        sm = c.get("split_mode", "percentage")
        if isinstance(ss, str):
            try: ss = json.loads(ss)
            except: ss = {}
        subj_txt = " | ".join(f'{s}:{p:.0f}%' for s, p in ss.items()) if ss else c.get("subjects_list", "")
        asmt_txt = f"Grade: {c['grade_pct']}% | Mult: {c['performance_multiplier']}x" if c.get("grade_pct") else "Pending"
        fpr_tag = ' <span class="skill-capsule" style="font-size:11px">FPR</span>' if c.get("has_fpr") else ""
        asmt_tag = ' <span class="skill-capsule" style="font-size:11px;background:rgba(251,191,36,0.12);color:#fbbf24;border-color:rgba(251,191,36,0.25)">Assessment</span>' if c.get("has_assessment") else ""
        st.markdown(f'<div class="glass-card" style="padding:18px"><div style="display:flex;justify-content:space-between"><span style="font-size:18px;font-weight:700;color:var(--text-primary)">{c["course_name"]}{fpr_tag}{asmt_tag}</span><span style="font-size:15px;color:var(--accent-cyan)">{len(cp)} sessions | {round(cm/60,1)}h</span></div><div style="font-size:14px;color:var(--text-secondary);margin-top:6px">{subj_txt}</div><div style="font-size:14px;color:var(--text-muted);margin-top:3px">{c.get("start_date","")} to {c.get("end_date","")} | {"% Split" if sm=="percentage" else "Lesson Split"} | {asmt_txt}</div></div>', unsafe_allow_html=True)

    # Weekly Attendance Chart with better x-axis formatting
    if present:
        st.markdown('<div class="section-title">Weekly Attendance</div>', unsafe_allow_html=True)
        df = pd.DataFrame(present)
        df["att_date"] = pd.to_datetime(df["att_date"])
        df["week_start"] = df["att_date"].dt.to_period("W").apply(lambda r: r.start_time)
        df["week_label"] = df["week_start"].dt.strftime("%d %b")
        cnames = {a["course_id"]: a.get("course_name", "") for a in present}
        df["course"] = df["course_id"].map(cnames)
        wk = df.groupby(["week_label", "week_start", "course"]).size().reset_index(name="sessions")
        wk = wk.sort_values("week_start")
        fig = px.bar(wk, x="week_label", y="sessions", color="course", barmode="stack", color_discrete_sequence=PAL)
        fig.update_layout(**_plt(title="Weekly Sessions by Course", height=340,
            xaxis=dict(tickangle=-45, tickfont=dict(color="#cbd5e1", size=12), title="Week Starting")))
        st.plotly_chart(fig, use_container_width=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CALCULATION PIPELINE — L1/L2 table matching v3 exactly + category capsules
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_calculations():
    st.markdown('<div class="page-title">Calculation Pipeline</div><div class="page-subtitle">11-Level XP hierarchy — unified tables with decay</div>', unsafe_allow_html=True)
    sid = st.session_state.selected_student
    if not sid: st.info("Select a student."); return
    xp = _build_engine(sid)
    if not xp: st.warning("No data."); return
    att = get_student_attendance(sid); courses = get_student_courses(sid)
    cmap = {c["course_id"]: c for c in courses}
    st.markdown(f'<div class="glass-card" style="padding:18px"><div style="font-size:18px;font-weight:700;color:var(--text-primary)">Pipeline: {xp["student"]["student_name"]}</div><div style="font-size:14px;color:var(--text-secondary)">L1→L2→L3→L4→L5→L6→L7→L8→L9→L10→L11</div></div>', unsafe_allow_html=True)

    # ── L1/L2 unified table with per-category + per-category decay columns (matching v3)
    st.markdown('<div class="section-title">L1/L2: XP Units & Sub-Units with Decay</div>', unsafe_allow_html=True)
    rows = []
    blocks_l = [{"block_id": c["course_id"], "student_id": sid, "course_id": c["course_id"],
                 "course_name": c["course_name"], "block_name": c["course_name"],
                 "is_active": c.get("is_active", 1), "performance_multiplier": c.get("performance_multiplier", 1.0)} for c in courses]
    att_copy = [{**a, "block_id": a["course_id"]} for a in att]
    asmts = get_student_assessments(sid)
    from xp_engine import XPCalculationEngine as XPCE
    eng_obj = XPCE(get_student(sid), blocks_l, att_copy, asmts)

    for a in att:
        if a["att_status"] != "present": continue
        su = a.get("sub_units", {})
        mult = a.get("performance_multiplier", 1.0)
        if isinstance(su, str):
            try: su = json.loads(su)
            except: su = {}
        crs = cmap.get(a["course_id"], {})
        is_act = bool(crs.get("is_active", 1))
        total_su_live = 0; total_su_decay = 0
        row = {"Date": a["att_date"], "Course": a.get("course_name", ""),
               "Subjects": a.get("subjects_list", ""),
               "Min": a["minutes_attended"],
               "L2 Raw": round(a["xp_unit_raw"], 4), "Mult": mult,
               "L2 Adj": round(a["xp_unit_adjusted"], 4)}
        for cat in CATEGORIES:
            v = su.get(cat, 0)
            cat_short = CATEGORY_DISPLAY.get(cat, cat)[:6]
            if v > 0:
                lv, dv = eng_obj.calc_decay_for_sub_unit(v, a["att_date"], cat, is_act)
                row[cat_short] = round(v, 4)
                row[f"{cat_short} D"] = round(dv, 4)
                total_su_live += lv; total_su_decay += dv
            else:
                row[cat_short] = "None"
                row[f"{cat_short} D"] = "None"
        row["L2 Decay"] = round(total_su_decay, 4)
        row["L2 Live"] = round(total_su_live, 4)
        rows.append(row)
    if rows:
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True, height=min(500, len(rows)*35+60))
        st.caption("'D' columns show decayed amount. L2 Decay = total XP unit decay.")

    # ── L3-L5 Course Aggregation table
    st.markdown('<div class="section-title">Course Aggregation (L3-L5)</div>', unsafe_allow_html=True)
    if xp.get("courses"):
        cd = [{"Course": cr["course_name"], "Subjects": ", ".join(cr["subjects"]),
               "Sessions": cr["sessions"], "Hours": cr["hours"],
               "Earned": round(cr["xp_earned"], 4), "Decayed": round(cr["xp_decayed"], 4),
               "Live": round(cr["xp_live"], 4)} for _, cr in xp["courses"].items()]
        st.dataframe(pd.DataFrame(cd), use_container_width=True, hide_index=True)

    # ── L4 Course Category Split CAPSULES (restored from v3)
    if xp.get("courses"):
        for _, cr in xp["courses"].items():
            ce = {c: round(v, 4) for c, v in cr["cat_earned"].items() if v > 0}
            if not ce: continue
            tot = cr["xp_earned"]
            ch = ""
            for c, e in ce.items():
                lv = cr["cat_live"].get(c, 0)
                pct = round(e / tot * 100, 1) if tot > 0 else 0
                col = CC.get(c, "#60a5fa")
                ch += f'<div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid rgba(100,160,255,0.06)"><span style="color:{col};font-weight:600;font-size:15px">{CATEGORY_DISPLAY.get(c,c)}</span><span style="color:var(--text-secondary);font-size:14px">{e} earned | {round(lv,4)} live | {pct}%</span></div>'
            st.markdown(f'<div class="glass-card-sm" style="padding:16px"><div style="display:flex;justify-content:space-between;margin-bottom:8px"><span style="font-size:16px;font-weight:700;color:var(--text-primary)">{cr["course_name"]}</span><span style="color:var(--accent-cyan);font-weight:700;font-size:16px">{tot:.4f} XP</span></div>{ch}</div>', unsafe_allow_html=True)

    # ── L6-L8 Category Aggregation
    st.markdown('<div class="section-title">Category Aggregation (L6-L8)</div>', unsafe_allow_html=True)
    catd = [{"Category": xp["categories"][c]["display_name"],
             "Earned": round(xp["categories"][c]["cat_xp_earned"], 4),
             "Decayed": round(xp["categories"][c]["cat_xp_decayed"], 4),
             "Live": round(xp["categories"][c]["cat_xp_live"], 4),
             "Level": xp["categories"][c]["cat_level"]} for c in CATEGORIES if xp["categories"][c]["cat_xp_earned"] > 0]
    if catd: st.dataframe(pd.DataFrame(catd), use_container_width=True, hide_index=True)

    # ── L9-L11 Student Total
    st.markdown('<div class="section-title">Student Total (L9-L11)</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(metric_card(f'{xp["total_xp_earned"]:.4f}', "Earned (L9)"), unsafe_allow_html=True)
    with c2: st.markdown(metric_card(f'{xp["total_xp_decayed"]:.4f}', "Decayed (L11)", "metric-red"), unsafe_allow_html=True)
    with c3: st.markdown(metric_card(f'{xp["total_xp_live"]:.4f}', "Live (L10)", "metric-green"), unsafe_allow_html=True)

    # ── Subject Levels (CALC-012) with Sessions and Hours (matching v3)
    st.markdown('<div class="section-title">Subject Levels (CALC-012)</div>', unsafe_allow_html=True)
    sd = [{"Subject": s, "XP Live": round(sr["xp_live"], 4), "XP Earned": round(sr["xp_earned"], 4),
           "Level": sr["level"], "Badge": sr["badge"] or "—",
           "Sessions": sr["sessions"], "Hours": sr["hours"]}
          for s, sr in sorted(xp["subjects"].items(), key=lambda x: x[1]["xp_live"], reverse=True)]
    if sd: st.dataframe(pd.DataFrame(sd), use_container_width=True, hide_index=True)

    # ── Engagement capsule (restored from v3)
    st.markdown(f'<div class="glass-card-sm" style="padding:16px"><span style="font-weight:700;font-size:16px;color:var(--text-primary)">Engagement:</span> <span style="color:var(--accent-cyan);font-size:24px;font-weight:800">{xp["engagement_score"]}</span><span style="color:var(--text-secondary);font-size:15px"> / 100 | Balance: {xp["balance_score"]} | Streak: {xp["streak_current"]}w | Efficiency: {xp["xp_efficiency"]} XP/hr</span></div>', unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SKILLS CALCULATION — with dynamic axis range
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_skills_calc():
    st.markdown('<div class="page-title">Skills Calculation</div><div class="page-subtitle">FPR & Assessment — Oliver\'s Calculation Framework (F-01 → F-06)</div>', unsafe_allow_html=True)
    sid = st.session_state.selected_student
    if not sid: st.info("Select a student."); return
    sk = _build_skills(sid)
    if not sk: st.info("No FPR or Assessment data for this student. Add FPR/Assessment when creating a course profile."); return

    # ── Per-Course Tables
    for cid, cdata in sk["per_course"].items():
        cname = cdata["course_name"]
        base_xp = cdata["base_xp"]
        st.markdown(f'<div class="section-title">{cname}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:14px;color:var(--text-secondary);margin-bottom:12px">{cdata["num_lessons"]} Lessons → Base XP: {base_xp}</div>', unsafe_allow_html=True)

        if cdata["has_fpr"]:
            st.markdown("**Final Progress Report — Learning Objectives**")
            fpr_rows = []
            for lo in cdata["fpr_los"]:
                skills = lo.get("skills", [])
                if isinstance(skills, str):
                    try: skills = json.loads(skills)
                    except: skills = []
                fpr_rows.append({
                    "Learning Objective": lo.get("lo_name", ""),
                    "Skill": ", ".join(skills),
                    "XP Weight": round(lo.get("xp_weight", 0), 3),
                    "Max Score": lo.get("max_score", 5),
                    "Actual Score": lo.get("actual_score", 0),
                    "% Score": f'{lo.get("pct_score", 0)*100:.1f}%',
                })
            if fpr_rows: st.dataframe(pd.DataFrame(fpr_rows), use_container_width=True, hide_index=True)

        if cdata["has_assessment"]:
            st.markdown("**Assessment — Sections**")
            asmt_rows = []
            for sec in cdata["asmt_sections"]:
                skills = sec.get("skills", [])
                if isinstance(skills, str):
                    try: skills = json.loads(skills)
                    except: skills = []
                asmt_rows.append({
                    "Section": sec.get("section_name", ""),
                    "Skill": ", ".join(skills),
                    "XP Weight": round(sec.get("xp_weight", 0), 3),
                    "Max Score": sec.get("max_score", 5),
                    "Actual Score": sec.get("actual_score", 0),
                    "% Score": f'{sec.get("pct_score", 0)*100:.1f}%',
                })
            if asmt_rows: st.dataframe(pd.DataFrame(asmt_rows), use_container_width=True, hide_index=True)

        # Course-level skill aggregate capsules
        if cdata["skill_aggregate"]:
            st.markdown("**Course Skill Aggregate**")
            caps = ""
            for skill_name, sdata in sorted(cdata["skill_aggregate"].items()):
                pct = sdata["avg_pct_score"]
                sc = _score_class(pct)
                caps += f'<div class="glass-card-skill" style="display:inline-block;min-width:170px;margin:6px;text-align:center;vertical-align:top"><div style="font-size:15px;font-weight:700;color:var(--text-primary)">{skill_name}</div><div class="score-pill {sc}" style="margin:8px 0">{pct*100:.1f}%</div><div style="font-size:12px;color:var(--text-muted)">XP Weight: {sdata["total_xp_weight"]:.2f}</div></div>'
            st.markdown(f'<div style="display:flex;flex-wrap:wrap;gap:4px">{caps}</div>', unsafe_allow_html=True)

    # ── CROSS-COURSE AGGREGATION
    if sk["cross_course_rows"]:
        st.markdown('<div class="section-title">Cross-Course Aggregation (All Skill-Rows)</div>', unsafe_allow_html=True)
        cross_df = []
        for r in sk["cross_course_rows"]:
            cross_df.append({
                "Skill": r["skill"], "Course": r.get("course_name", ""),
                "Source": r["source"],
                "% Score": f'{r["pct_score"]*100:.1f}%',
                "XP Weight": round(r["xp_weight"], 3),
                "Earned XP": round(r["weighted_score"], 3),
            })
        st.dataframe(pd.DataFrame(cross_df), use_container_width=True, hide_index=True)

    # ── FINAL OUTPUT
    if sk["final_output"]:
        st.markdown('<div class="section-title">Final Output — Both Metrics Per Skill</div>', unsafe_allow_html=True)
        final_rows = []
        for skill_name, fdata in sorted(sk["final_output"].items()):
            final_rows.append({
                "Skill": skill_name,
                "Avg Skill Score (F-05)": f'{fdata["avg_skill_score"]*100:.2f}%',
                "Avg Skill Weighted XP Score (F-06)": f'{fdata["avg_skill_wtd_xp_score"]*100:.2f}%',
                "Total XP Weight": round(fdata["total_xp_weight"], 3),
                "Total Earned XP": round(fdata["total_weighted_score"], 3),
            })
        st.dataframe(pd.DataFrame(final_rows), use_container_width=True, hide_index=True)

        # ── Skill Performance Comparison with DYNAMIC axis range
        st.markdown('<div class="section-title">Skill Performance Comparison</div>', unsafe_allow_html=True)
        skills_sorted = sorted(sk["final_output"].items(), key=lambda x: x[1]["avg_skill_score"], reverse=True)
        snames = [s[0] for s in skills_sorted]
        f05 = [s[1]["avg_skill_score"]*100 for s in skills_sorted]
        f06 = [s[1]["avg_skill_wtd_xp_score"]*100 for s in skills_sorted]
        # Dynamic lower limit: floor to nearest 5 below minimum
        all_vals = f05 + f06
        min_val = min(all_vals) if all_vals else 0
        axis_min = max(0, math.floor(min_val / 5) * 5 - 5)
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Avg Skill Score (F-05)", y=snames, x=f05, orientation="h",
            marker=dict(color="#818cf8", cornerradius=4),
            text=[f"{v:.1f}%" for v in f05], textposition="inside", textfont=dict(size=13, color="white")))
        fig.add_trace(go.Bar(name="Avg Weighted XP Score (F-06)", y=snames, x=f06, orientation="h",
            marker=dict(color="#2dd4bf", cornerradius=4),
            text=[f"{v:.1f}%" for v in f06], textposition="inside", textfont=dict(size=13, color="white")))
        fig.update_layout(**_plt(barmode="group", height=max(280, len(snames)*55),
            yaxis=dict(autorange="reversed"),
            xaxis=dict(range=[axis_min, 100], title="Score %"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)))
        st.plotly_chart(fig, use_container_width=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# XP OVERVIEW — fully restored from v3 with all metrics
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_xp_dashboard():
    st.markdown('<div class="page-title">XP Overview</div><div class="page-subtitle">Student status, badges, tiers, and XP aggregate summary</div>', unsafe_allow_html=True)
    sid = st.session_state.selected_student
    if not sid: st.info("Select a student."); return
    xp = _build_engine(sid)
    if not xp: return
    ns = xp["next_status"]; nn = ns["name"] if ns else "Max"
    xr = round(ns["min_xp"] - xp["total_xp_live"], 2) if ns else 0

    # ── Status Hero Card
    st.markdown(f'<div class="glass-card" style="text-align:center;padding:28px"><div style="font-size:14px;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.12em">Student Status</div><div style="font-size:46px;font-weight:800;color:var(--accent-cyan);margin:6px 0">Level {xp["status_level"]}</div><div style="font-size:26px;font-weight:600;color:var(--text-primary);margin-bottom:14px">{xp["status_name"]}</div>{progress_bar(xp["status_pct"])}<div style="font-size:15px;color:var(--text-muted);margin-top:8px">{xp["status_pct"]}% to {nn} ({xr} XP remaining)</div></div>', unsafe_allow_html=True)

    # ── 2 rows × 4 metrics (matching v3)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(metric_card(f'{xp["total_xp_live"]:.2f}', "Live XP", "metric-green"), unsafe_allow_html=True)
    with c2: st.markdown(metric_card(f'{xp["total_xp_earned"]:.2f}', "Total Earned", "metric-cyan"), unsafe_allow_html=True)
    with c3: st.markdown(metric_card(xp["total_hours"], "Study Hours", "metric-orange"), unsafe_allow_html=True)
    with c4: st.markdown(metric_card(f'{xp["engagement_score"]}', "Engagement", "metric-purple"), unsafe_allow_html=True)
    c5, c6, c7, c8 = st.columns(4)
    with c5: st.markdown(metric_card(xp["total_sessions"], "Attended", "metric-green"), unsafe_allow_html=True)
    with c6: st.markdown(metric_card(f'{xp["xp_efficiency"]}', "XP/Hour", "metric-cyan"), unsafe_allow_html=True)
    with c7: st.markdown(metric_card(f'{xp["decay_pct"]}%', "XP Decayed", "metric-red"), unsafe_allow_html=True)
    with c8: st.markdown(metric_card(f'{xp["streak_current"]}w', "Streak", "metric-gold"), unsafe_allow_html=True)

    # ── Category Overview: Radar + Donut
    st.markdown('<div class="section-title">Category Overview</div>', unsafe_allow_html=True)
    cr_col, cd_col = st.columns([1, 1])
    with cr_col:
        vals = [xp["categories"][c]["cat_xp_live"] for c in CATEGORIES]
        labs = [CATEGORY_DISPLAY.get(c, c) for c in CATEGORIES]
        fig = go.Figure(go.Scatterpolar(r=vals+[vals[0]], theta=labs+[labs[0]], fill="toself",
            fillcolor="rgba(251,191,36,0.12)", line=dict(color="#fbbf24", width=2), marker=dict(size=6)))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#e2e8f0", size=13),
            margin=dict(l=60, r=60, t=30, b=30),
            polar=dict(bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(visible=True, gridcolor="rgba(100,160,255,0.1)", tickfont=dict(color="#94a3b8", size=11)),
                angularaxis=dict(gridcolor="rgba(100,160,255,0.15)", tickfont=dict(color="#e2e8f0", size=13))),
            showlegend=False, height=360)
        st.plotly_chart(fig, use_container_width=True)
    with cd_col:
        ac = [(c, xp["categories"][c]["cat_xp_live"]) for c in CATEGORIES if xp["categories"][c]["cat_xp_live"] > 0]
        if ac:
            fig = go.Figure(go.Pie(
                labels=[CATEGORY_DISPLAY.get(c, c) for c, _ in ac], values=[v for _, v in ac],
                hole=0.55, marker=dict(colors=[CC.get(c, "#60a5fa") for c, _ in ac]),
                textinfo="label+percent", textposition="outside",
                textfont=dict(size=13, color="#e2e8f0"), pull=[0.03]*len(ac)))
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e2e8f0"),
                margin=dict(l=20, r=20, t=20, b=20), showlegend=False, height=360)
            st.plotly_chart(fig, use_container_width=True)

    # ── 6 Category Level Cards
    cat_cols = st.columns(6)
    for i, cat in enumerate(CATEGORIES):
        cv = xp["categories"][cat]; color = CC.get(cat, "#60a5fa")
        with cat_cols[i]:
            st.markdown(f'<div class="glass-card-sm" style="text-align:center;padding:14px"><div style="font-size:28px;font-weight:800;color:{color}">L{cv["cat_level"]}</div><div style="font-size:12px;color:var(--text-muted);text-transform:uppercase;margin:3px 0">{cv["display_name"]}</div><div style="font-size:14px;color:var(--text-secondary)">{cv["cat_xp_live"]:.2f} XP</div>{progress_bar(cv["cat_level_pct"])}</div>', unsafe_allow_html=True)

    # ── Projected Growth (from v3)
    st.markdown('<div class="section-title">Projected Growth</div>', unsafe_allow_html=True)
    wr = round(xp["total_xp_earned"] / (max(1, xp["total_sessions"]) / 2.5), 4) if xp["total_sessions"] > 0 else 0
    ew = round(xr / wr) if wr > 0 else 999
    strongest = CATEGORY_DISPLAY.get(xp["strongest_cat"], "—") if xp["strongest_cat"] else "—"
    weakest = CATEGORY_DISPLAY.get(xp["weakest_cat"], "—") if xp["weakest_cat"] else "—"
    st.markdown(f'<div class="glass-card" style="padding:18px;font-size:15px;line-height:2.2;color:var(--text-secondary)">Weekly XP Rate: <b style="color:var(--accent-green)">{wr:.3f} XP/wk</b><br>XP to Next ({nn}): <b style="color:var(--accent-orange)">{xr} XP</b><br>Est. Time: <b style="color:var(--accent-cyan)">~{ew} weeks</b><br>Strongest: <b style="color:var(--accent-green)">{strongest}</b> | Needs Attention: <b style="color:var(--accent-red)">{weakest}</b></div>', unsafe_allow_html=True)

    # ── Course Performance Comparison (with Decayed bar from v3)
    if xp.get("courses") and len(xp["courses"]) > 1:
        st.markdown('<div class="section-title">XP — Course Performance Comparison</div>', unsafe_allow_html=True)
        cn = [cr["course_name"] for cr in xp["courses"].values()]
        ce = [round(cr["xp_earned"], 2) for cr in xp["courses"].values()]
        cl = [round(cr["xp_live"], 2) for cr in xp["courses"].values()]
        cd3 = [round(cr["xp_decayed"], 2) for cr in xp["courses"].values()]
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Earned", x=cn, y=ce, marker=dict(color="#818cf8"), opacity=0.85,
            text=[f"{v:.1f}" for v in ce], textposition="auto", textfont=dict(color="white", size=12)))
        fig.add_trace(go.Bar(name="Live", x=cn, y=cl, marker=dict(color="#2dd4bf"), opacity=0.9,
            text=[f"{v:.1f}" for v in cl], textposition="auto", textfont=dict(color="white", size=12)))
        fig.add_trace(go.Bar(name="Decayed", x=cn, y=cd3, marker=dict(color="#fb7185"), opacity=0.85,
            text=[f"{v:.1f}" for v in cd3], textposition="auto", textfont=dict(color="white", size=12)))
        fig.update_layout(**_plt(barmode="group", height=380))
        st.plotly_chart(fig, use_container_width=True)

    # ── Subject Levels & Badges (with level_pct from v3)
    st.markdown('<div class="section-title">Subject Levels & Badges</div>', unsafe_allow_html=True)
    for subj, sr in sorted(xp["subjects"].items(), key=lambda x: x[1]["xp_live"], reverse=True):
        bc = {"Bronze": "orange", "Silver": "purple", "Gold": "gold"}.get(sr["badge"], "blue") if sr["badge"] else "blue"
        bt = sr["badge"] or "—"
        col = PAL[hash(subj) % len(PAL)]
        st.markdown(f'<div class="glass-card-sm" style="display:flex;justify-content:space-between;align-items:center;padding:14px;border-left:4px solid {col}"><div><span style="font-size:16px;font-weight:600;color:var(--text-primary)">{subj}</span> {badge_html(bt,bc)}</div><div style="text-align:right"><div style="font-size:15px;font-weight:700;color:var(--accent-cyan)">Level {sr["level"]} | {sr["xp_live"]:.2f} XP</div><div style="font-size:13px;color:var(--text-muted)">{sr["level_pct"]}% | {sr["sessions"]}s | {sr["hours"]}h</div></div></div>', unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# INSIGHTS & CHARTS — fully restored v3 + premium skills analysis
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_insights():
    st.markdown('<div class="page-title">Insights & Charts</div><div class="page-subtitle">Premium data storytelling — XP, Skills & Activity Analysis</div>', unsafe_allow_html=True)
    sid = st.session_state.selected_student
    if not sid: st.info("Select a student."); return
    xp = _build_engine(sid)
    if not xp: return
    att = get_student_attendance(sid)
    present = sorted([a for a in att if a["att_status"] == "present"], key=lambda x: x["att_date"])

    # ── Monthly XP Trend (from v3)
    if xp["monthly_xp"]:
        st.markdown('<div class="section-title">Monthly XP Earned</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Scatter(x=list(xp["monthly_xp"].keys()), y=list(xp["monthly_xp"].values()),
            mode="lines+markers", line=dict(color="#818cf8", width=3, shape="spline"),
            fill="tozeroy", fillcolor="rgba(129,140,248,0.08)",
            marker=dict(size=8, color="#818cf8", line=dict(width=2, color="#fff"))))
        fig.update_layout(**_plt(height=320))
        st.plotly_chart(fig, use_container_width=True)

    # ── Course Breakdown — horizontal stacked (from v3 with text labels)
    if xp.get("courses"):
        st.markdown('<div class="section-title">XP — Course Breakdown</div>', unsafe_allow_html=True)
        cn = [cr["course_name"] for cr in xp["courses"].values()]
        cl = [round(cr["xp_live"], 2) for cr in xp["courses"].values()]
        cd4 = [round(cr["xp_decayed"], 2) for cr in xp["courses"].values()]
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Live XP", y=cn, x=cl, orientation="h",
            marker=dict(color="#2dd4bf", cornerradius=4),
            text=[f"{v:.1f}" for v in cl], textposition="inside", textfont=dict(size=13, color="white")))
        fig.add_trace(go.Bar(name="Decayed", y=cn, x=cd4, orientation="h",
            marker=dict(color="#fb7185", cornerradius=4),
            text=[f"{v:.1f}" for v in cd4], textposition="inside", textfont=dict(size=13, color="white")))
        fig.update_layout(**_plt(barmode="stack", height=max(200, len(cn)*70),
            yaxis=dict(autorange="reversed"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)))
        st.plotly_chart(fig, use_container_width=True)

    # ── Subject XP Bars (from v3 with decay)
    st.markdown('<div class="section-title">XP by Subject</div>', unsafe_allow_html=True)
    sn_list = sorted(xp["subjects"].keys(), key=lambda s: xp["subjects"][s]["xp_live"], reverse=True)
    sl = [round(xp["subjects"][s]["xp_live"], 2) for s in sn_list]
    sd_list = [round(xp["subjects"][s]["xp_earned"] - xp["subjects"][s]["xp_live"], 2) for s in sn_list]
    fig = go.Figure()
    for i, (name, live, decay) in enumerate(zip(sn_list, sl, sd_list)):
        col = PAL[i % len(PAL)]
        fig.add_trace(go.Bar(name=name if i < 8 else None, y=[name], x=[live], orientation="h",
            marker=dict(color=col, cornerradius=6),
            text=[f"{live:.1f}"], textposition="inside", textfont=dict(size=12, color="white"), showlegend=i < 8))
        if decay > 0.01:
            fig.add_trace(go.Bar(name="Decayed" if i == 0 else None, y=[name], x=[decay], orientation="h",
                marker=dict(color="#fb7185", opacity=0.5, cornerradius=6), showlegend=i == 0))
    fig.update_layout(**_plt(barmode="stack", height=max(250, len(sn_list)*45),
        yaxis=dict(autorange="reversed"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)))
    st.plotly_chart(fig, use_container_width=True)

    # ── Cumulative Decay Over Time (from v3)
    st.markdown('<div class="section-title">Cumulative XP Decay Over Time</div>', unsafe_allow_html=True)
    if present:
        cum = 0; dx = []; dy = []
        for a in present:
            cum += a.get("xp_unit_adjusted", 0); dx.append(a["att_date"]); dy.append(round(cum, 4))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dx, y=dy, name="Cumulative Earned", mode="lines+markers",
            line=dict(color="#60a5fa", width=2), marker=dict(size=4)))
        fig.add_hline(y=xp["total_xp_live"], line_dash="dash", line_color="#34d399",
            annotation_text=f'Live: {xp["total_xp_live"]:.2f}',
            annotation_font=dict(color="#34d399", size=14))
        fig.update_layout(**_plt(height=360))
        st.plotly_chart(fig, use_container_width=True)

    # ── XP Activity Heatmap — GitHub-style (from v3)
    st.markdown('<div class="section-title">XP Activity Heatmap</div>', unsafe_allow_html=True)
    if present:
        df_h = pd.DataFrame(present); df_h["att_date"] = pd.to_datetime(df_h["att_date"])
        daily = df_h.groupby(df_h["att_date"].dt.date).agg(xp=("xp_unit_adjusted", "sum"), sessions=("attendance_id", "count")).reset_index()
        daily.columns = ["date", "xp", "sessions"]; daily["date"] = pd.to_datetime(daily["date"])
        d_min = daily["date"].min(); d_max = daily["date"].max()
        full_df = pd.DataFrame({"date": pd.date_range(d_min, d_max, freq="D")})
        full_df = full_df.merge(daily, on="date", how="left").fillna(0)
        full_df["dow"] = full_df["date"].dt.dayofweek
        full_df["year_week"] = full_df["date"].dt.strftime("%Y-W%W")
        weeks = sorted(full_df["year_week"].unique())
        dow_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        z_matrix = []; hover_matrix = []
        for dow in range(7):
            row = []; hrow = []
            for w in weeks:
                match = full_df[(full_df["year_week"] == w) & (full_df["dow"] == dow)]
                if len(match) > 0:
                    val = match.iloc[0]["xp"]; dt = match.iloc[0]["date"].strftime("%b %d"); sess = int(match.iloc[0]["sessions"])
                    row.append(val); hrow.append(f"{dt}<br>{val:.2f} XP | {sess}s")
                else: row.append(0); hrow.append("")
            z_matrix.append(row); hover_matrix.append(hrow)
        if len(weeks) > 52: weeks = weeks[-52:]; z_matrix = [r[-52:] for r in z_matrix]; hover_matrix = [r[-52:] for r in hover_matrix]
        month_ticks = []; month_labels = []; seen_months = set()
        for i, w in enumerate(weeks):
            try:
                yr = int(w[:4]); wk = int(w.split("W")[1])
                d = datetime.strptime(f"{yr}-W{wk:02d}-1", "%Y-W%W-%w")
                ml = d.strftime("%b '%y")
                if ml not in seen_months: month_ticks.append(i); month_labels.append(ml); seen_months.add(ml)
            except: pass
        fig = go.Figure(go.Heatmap(z=z_matrix, x=list(range(len(weeks))), y=dow_labels,
            hovertext=hover_matrix, hoverinfo="text",
            colorscale=[[0, "#0f1629"], [0.01, "#1a2747"], [0.25, "#1e4d7b"], [0.5, "#2563eb"], [0.75, "#60a5fa"], [1.0, "#93c5fd"]],
            showscale=False, xgap=2, ygap=2))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#e2e8f0", size=12), margin=dict(l=40, r=10, t=10, b=40), height=200,
            xaxis=dict(tickvals=month_ticks, ticktext=month_labels, showgrid=False, tickfont=dict(color="#cbd5e1", size=12)),
            yaxis=dict(showgrid=False, autorange="reversed", tickfont=dict(color="#cbd5e1", size=12)))
        st.plotly_chart(fig, use_container_width=True)

    # ── Subject-Category XP Sunburst (from v3)
    st.markdown('<div class="section-title">Subject-Category XP Sunburst</div>', unsafe_allow_html=True)
    sb_ids = []; sb_labels = []; sb_parents = []; sb_values = []; sb_colors = []
    sb_ids.append("Total"); sb_labels.append(f"Total<br>{xp['total_xp_live']:.1f} XP")
    sb_parents.append(""); sb_values.append(xp["total_xp_live"]); sb_colors.append("#1a2340")
    for cat in CATEGORIES:
        cv = xp["categories"][cat]
        if cv["cat_xp_live"] > 0:
            sb_ids.append(cat); sb_labels.append(f"{cv['display_name']}<br>{cv['cat_xp_live']:.1f} XP")
            sb_parents.append("Total"); sb_values.append(cv["cat_xp_live"]); sb_colors.append(CC.get(cat, "#60a5fa"))
    for subj, sr in xp["subjects"].items():
        if sr["xp_live"] > 0:
            cfg = SUBJECT_CATEGORY_CONFIG.get(subj, {})
            best_cat = max(CATEGORIES, key=lambda c: cfg.get(c, 0))
            if xp["categories"][best_cat]["cat_xp_live"] > 0:
                sb_ids.append(f"{subj}_{best_cat}"); sb_labels.append(f"{subj}<br>L{sr['level']} {sr['xp_live']:.1f}")
                sb_parents.append(best_cat); sb_values.append(sr["xp_live"]); sb_colors.append(CC.get(best_cat, "#60a5fa"))
    fig = go.Figure(go.Sunburst(ids=sb_ids, labels=sb_labels, parents=sb_parents, values=sb_values,
        marker=dict(colors=sb_colors), branchvalues="total",
        textfont=dict(size=12, color="white"), hovertemplate="<b>%{label}</b><extra></extra>"))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=10, b=10), height=450)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Interactive sunburst: Total XP → Category → Subject hierarchy. Click to drill down.")

    # ── Category Momentum 4-Week (from v3)
    st.markdown('<div class="section-title">Category Momentum (4-Week)</div>', unsafe_allow_html=True)
    vel = [(CATEGORY_DISPLAY.get(c, c), xp["cat_velocity"].get(c, 0), CC.get(c, "#60a5fa")) for c in CATEGORIES if xp["cat_velocity"].get(c, 0) > 0]
    vel.sort(key=lambda x: x[1], reverse=True)
    if vel:
        mx = max(v[1] for v in vel)
        for nm, vl, col in vel:
            bp = vl / mx * 100 if mx > 0 else 0
            st.markdown(f'<div class="glass-card-sm" style="padding:12px"><div style="display:flex;justify-content:space-between;margin-bottom:3px"><span style="font-weight:600;font-size:15px;color:{col}">{nm}</span><span style="font-weight:700;font-size:15px;color:var(--text-primary)">{vl:.3f} XP/wk</span></div><div style="background:rgba(15,22,41,0.6);border-radius:8px;height:8px;overflow:hidden"><div style="height:100%;border-radius:8px;background:{col};width:{bp}%"></div></div></div>', unsafe_allow_html=True)

    # ── NEW: Skills Analysis (premium charts)
    sk = _build_skills(sid)
    if sk and sk["final_output"]:
        st.markdown('<div class="section-title">Skills Performance — Radar Analysis</div>', unsafe_allow_html=True)
        skills_sorted = sorted(sk["final_output"].items(), key=lambda x: x[1]["avg_skill_score"], reverse=True)
        if len(skills_sorted) >= 3:
            labels = [s[0] for s in skills_sorted]
            f05 = [s[1]["avg_skill_score"]*100 for s in skills_sorted]
            f06 = [s[1]["avg_skill_wtd_xp_score"]*100 for s in skills_sorted]
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(r=f05+[f05[0]], theta=labels+[labels[0]], fill="toself",
                name="Avg Skill Score (F-05)", fillcolor="rgba(129,140,248,0.15)", line=dict(color="#818cf8", width=2)))
            fig.add_trace(go.Scatterpolar(r=f06+[f06[0]], theta=labels+[labels[0]], fill="toself",
                name="Avg Wtd XP Score (F-06)", fillcolor="rgba(45,212,191,0.15)", line=dict(color="#2dd4bf", width=2)))
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#e2e8f0", size=13), margin=dict(l=80, r=80, t=40, b=40),
                polar=dict(bgcolor="rgba(0,0,0,0)",
                    radialaxis=dict(visible=True, gridcolor="rgba(100,160,255,0.1)", range=[0, 100],
                        tickfont=dict(color="#94a3b8", size=11)),
                    angularaxis=dict(tickfont=dict(color="#e2e8f0", size=13))),
                height=420, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5, font=dict(color="#e2e8f0")))
            st.plotly_chart(fig, use_container_width=True)

        # ── Course × Skill Heatmap
        st.markdown('<div class="section-title">Course × Skill Performance Heatmap</div>', unsafe_allow_html=True)
        courses_with_skills = [c for c in sk["per_course"].values() if c["skill_aggregate"]]
        if courses_with_skills:
            all_skills = sorted(set(sk2 for c in courses_with_skills for sk2 in c["skill_aggregate"].keys()))
            cnames = [c["course_name"] for c in courses_with_skills]
            z = []
            for c in courses_with_skills:
                row = []
                for skill in all_skills:
                    val = c["skill_aggregate"].get(skill, {}).get("avg_pct_score", None)
                    row.append(round(val*100, 1) if val is not None else None)
                z.append(row)
            fig = go.Figure(go.Heatmap(z=z, x=all_skills, y=cnames,
                colorscale=[[0, "#1a2747"], [0.4, "#f59e0b"], [0.7, "#34d399"], [1, "#22d3ee"]],
                showscale=True, colorbar=dict(tickfont=dict(color="#e2e8f0")),
                text=[[f"{v:.0f}%" if v else "" for v in row] for row in z],
                texttemplate="%{text}", textfont=dict(size=13, color="white"), xgap=3, ygap=3))
            fig.update_layout(**_plt(height=max(220, len(cnames)*65+80),
                xaxis=dict(side="top", tickfont=dict(color="#e2e8f0", size=13)),
                yaxis=dict(tickfont=dict(color="#e2e8f0", size=13))))
            st.plotly_chart(fig, use_container_width=True)

        # ── Skill Score Distribution (Lollipop chart — F-06 Weighted XP Score)
        st.markdown('<div class="section-title">Skill Score Distribution (Weighted)</div>', unsafe_allow_html=True)
        sk_names = [s[0] for s in skills_sorted]
        sk_f06 = [s[1]["avg_skill_wtd_xp_score"]*100 for s in skills_sorted]
        fig = go.Figure()
        for i, (nm, val) in enumerate(zip(sk_names, sk_f06)):
            color = "#34d399" if val >= 70 else "#fbbf24" if val >= 40 else "#fb7185"
            fig.add_trace(go.Scatter(x=[val], y=[nm], mode="markers+text",
                marker=dict(size=16, color=color, line=dict(width=2, color="white")),
                text=[f"{val:.0f}%"], textposition="middle right", textfont=dict(color="#e2e8f0", size=13),
                showlegend=False))
            fig.add_shape(type="line", x0=0, x1=val, y0=nm, y1=nm,
                line=dict(color=color, width=3, dash="solid"))
        fig.update_layout(**_plt(height=max(250, len(sk_names)*45),
            xaxis=dict(range=[0, 105], title="Avg Skill Weighted XP Score (F-06)"),
            yaxis=dict(autorange="reversed")))
        st.plotly_chart(fig, use_container_width=True)

    # ── Key Insights (cleaned up — no "Study" confusion)
    st.markdown('<div class="section-title">Key Insights</div>', unsafe_allow_html=True)
    strongest = CATEGORY_DISPLAY.get(xp["strongest_cat"], "—") if xp["strongest_cat"] else "—"
    weakest = CATEGORY_DISPLAY.get(xp["weakest_cat"], "—") if xp["weakest_cat"] else "—"
    for lbl, val in [
        ("Strongest Category", strongest),
        ("Weakest Category", weakest),
        ("Active Categories", f'{xp["active_cats_count"]}/6'),
        ("Balance Score", f'{xp["balance_score"]}/100'),
        ("Total Study Hours", f'{xp["total_hours"]}h'),
        ("Total Sessions", f'{xp["total_sessions"]}'),
        ("XP Efficiency", f'{xp["xp_efficiency"]} XP/hr'),
        ("Current Streak", f'{xp["streak_current"]} weeks'),
    ]:
        st.markdown(f'<div class="glass-card-sm" style="padding:12px 18px;display:flex;justify-content:space-between"><span style="color:var(--text-secondary);font-size:15px">{lbl}</span><span style="color:var(--accent-cyan);font-weight:700;font-size:15px">{val}</span></div>', unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FINAL REPORT — Premium redesign
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_final_report():
    st.markdown('<div class="page-title">Final Report</div><div class="page-subtitle">Student Progress Report — Premium View</div>', unsafe_allow_html=True)
    sid = st.session_state.selected_student
    if not sid: st.info("Select a student."); return
    s = get_student(sid); courses = get_student_courses(sid)
    fpr_courses = [c for c in courses if c.get("has_fpr")]
    if not fpr_courses:
        st.info("No courses with Final Progress Report data."); return

    course_names = [c["course_name"] for c in fpr_courses]
    selected_course = st.selectbox("Select Course", course_names, key="fr_course")
    sel_c = next((c for c in fpr_courses if c["course_name"] == selected_course), None)
    if not sel_c: return
    los = get_course_fpr_los(sel_c["course_id"])
    asmt_secs = get_course_assessment_sections(sel_c["course_id"])
    if not los: st.info("No Learning Objectives found."); return

    grade_colors = {5: ("#059669", "#d1fae5", "Excellent"), 4: ("#0284c7", "#e0f2fe", "Good"),
                    3: ("#d97706", "#fef3c7", "Developing"), 2: ("#ea580c", "#ffedd5", "Needs Support"),
                    1: ("#dc2626", "#fee2e2", "Beginning")}

    # Group LOs by index
    lo_grouped = defaultdict(list)
    for lo in los: lo_grouped[lo["lo_index"]].append(lo)

    # ── Header
    report_html = f'''<div class="white-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding-bottom:16px;border-bottom:3px solid #e5e7eb">
        <div>
            <div style="font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:0.15em;font-weight:600">Linxed Learning</div>
            <div style="font-size:26px;font-weight:800;color:#111827;margin:4px 0">Final Progress Report</div>
            <div style="font-size:15px;color:#6b7280">{s["student_name"]}</div>
        </div>
        <div style="text-align:right">
            <div style="font-size:14px;font-weight:600;color:#111827">{selected_course}</div>
            <div style="font-size:13px;color:#6b7280">{sel_c.get("start_date","")} to {sel_c.get("end_date","")}</div>
            <div style="font-size:13px;color:#6b7280">{sel_c.get("num_lessons",0)} Lessons</div>
        </div>
    </div>
    <div style="display:flex;gap:24px;margin-bottom:20px">
        <div style="flex:1;padding:12px 16px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0">
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;font-weight:600">Grade Scale</div>
            <div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap">'''
    for g in [5, 4, 3, 2, 1]:
        gc, gbg, gl = grade_colors[g]
        report_html += f'<span style="padding:3px 10px;border-radius:8px;font-size:12px;font-weight:700;background:{gbg};color:{gc}">{g} = {gl}</span>'
    report_html += '''</div></div></div>'''

    # ── Learning Objectives
    for lo_idx in sorted(lo_grouped.keys()):
        lo_rows = lo_grouped[lo_idx]
        first = lo_rows[0]
        actual = int(first.get("actual_score", 0))
        max_s = int(first.get("max_score", 5))
        gc, gbg, gl = grade_colors.get(actual, ("#6b7280", "#f3f4f6", "—"))
        skills = set()
        for lr in lo_rows:
            sk = lr.get("skills", [])
            if isinstance(sk, str):
                try: sk = json.loads(sk)
                except: sk = []
            skills.update(sk)
        skills_html = "".join(f'<span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:rgba(59,130,246,0.08);color:#3b82f6;margin:2px">{sk}</span>' for sk in sorted(skills))
        report_html += f'''<div style="padding:16px 0;border-bottom:1px solid #f1f5f9;display:flex;align-items:center;gap:18px">
            <div style="min-width:56px;text-align:center"><div class="fpr-grade-box" style="background:{gbg};color:{gc}">{actual}</div><div style="font-size:10px;color:#9ca3af;margin-top:3px">/{max_s}</div></div>
            <div style="flex:1"><div style="font-size:15px;font-weight:600;color:#111827">{first.get("lo_name","")}</div><div style="margin-top:5px">{skills_html}</div></div>
            <div style="text-align:right;min-width:100px"><span style="padding:5px 14px;border-radius:8px;font-size:12px;font-weight:700;background:{gbg};color:{gc}">{gl}</span></div>
        </div>'''
    report_html += '</div>'
    st.markdown(report_html, unsafe_allow_html=True)

    # ── Assessment Results
    if asmt_secs:
        sec_grouped = defaultdict(list)
        for sec in asmt_secs: sec_grouped[sec["section_index"]].append(sec)
        asmt_html = '<div class="white-card"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid #e5e7eb"><div style="font-size:20px;font-weight:700;color:#111827">Assessment Results</div><div style="font-size:13px;color:#6b7280">Score breakdown by section</div></div>'
        for sidx in sorted(sec_grouped.keys()):
            sec_rows = sec_grouped[sidx]
            first = sec_rows[0]
            actual = first.get("actual_score", 0)
            max_s = first.get("max_score", 5)
            pct = first.get("pct_score", 0)
            skills = set()
            for sr in sec_rows:
                sk = sr.get("skills", [])
                if isinstance(sk, str):
                    try: sk = json.loads(sk)
                    except: sk = []
                skills.update(sk)
            pct_color = "#059669" if pct >= 0.7 else "#d97706" if pct >= 0.4 else "#dc2626"
            pct_bg = "#d1fae5" if pct >= 0.7 else "#fef3c7" if pct >= 0.4 else "#fee2e2"
            skills_html = "".join(f'<span style="padding:3px 8px;border-radius:10px;font-size:11px;font-weight:600;background:rgba(251,191,36,0.08);color:#b45309;margin:1px">{sk}</span>' for sk in sorted(skills))
            # Progress bar
            bar_width = pct * 100
            asmt_html += f'''<div style="padding:14px 0;border-bottom:1px solid #f1f5f9">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
                    <div><div style="font-size:14px;font-weight:600;color:#111827">{first.get("section_name","")}</div><div style="margin-top:3px">{skills_html}</div></div>
                    <div style="text-align:right"><span style="font-size:16px;font-weight:700;color:{pct_color}">{int(actual)}/{int(max_s)}</span><span style="padding:3px 10px;margin-left:8px;border-radius:8px;font-size:12px;font-weight:700;background:{pct_bg};color:{pct_color}">{pct*100:.0f}%</span></div>
                </div>
                <div style="background:#f1f5f9;border-radius:6px;height:6px;overflow:hidden"><div style="height:100%;border-radius:6px;background:{pct_color};width:{bar_width}%"></div></div>
            </div>'''
        asmt_html += '</div>'
        st.markdown(asmt_html, unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FORMULAS — XP + Skills (F-01 through F-06)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_formulas():
    st.markdown('<div class="page-title">Calculation Formulas</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">XP Calculation Pipeline</div>', unsafe_allow_html=True)
    for cid, name, formula, desc in [
        ("CALC-001", "XP Unit (L2)", "minutes × 0.01", "Raw XP per attendance."),
        ("CALC-002", "XP Sub-Units (L1)", "adjusted × Σ(share[s] × cat_split[s][c])", "Category breakdown via subject shares."),
        ("CALC-003", "Course XP Raw (L3)", "SUM(unit_raw)", "Raw XP per course."),
        ("CALC-004", "Course Category (L4)", "SUM(sub_units[c])", "Category earned per course."),
        ("CALC-005", "Performance Mult", "grade → band lookup", "1.0x / 1.25x / 1.5x. Per course assessment."),
        ("CALC-006", "Course Total (L5)", "raw × mult", "Course-level earned XP."),
        ("CALC-007", "Compound Decay", "cur × (1-rate) daily", "5 bands × active/inactive."),
        ("CALC-008", "Category Agg (L6-8)", "SUM(course_cat)", "Cross-course category totals."),
        ("CALC-009", "Student Total (L9-11)", "SUM(course_earned)", "Lifetime totals."),
        ("CALC-010", "Category Level", "LOOKUP(live)", "L0-L5."),
        ("CALC-011", "Student Status", "LOOKUP(live)", "L1-L8."),
        ("CALC-012", "Subject Level+Badge", "LOOKUP(live)", "31 levels. Bronze/Silver/Gold."),
        ("CALC-016", "Engagement", "0.30×cons + 0.25×bal + 0.25×str + 0.20×perf", "0-100 composite."),
        ("CALC-017", "Efficiency", "earned/hours", "XP per hour."),
        ("CALC-018", "Velocity", "SUM(28d cat XP)/4", "4-week rate."),
    ]:
        st.markdown(f'<div style="margin-bottom:14px"><div class="formula-title">{cid}: {name}</div><div class="formula-desc">{desc}</div><div class="formula-block">{formula}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Skills Calculation Framework (FPR & Assessment)</div>', unsafe_allow_html=True)
    for cid, name, formula, desc in [
        ("F-01a", "XP Weight per LO", "course_xp / num_LOs", "Evenly distributed XP across Learning Objectives."),
        ("F-01b", "XP Weight per Section", "course_xp / num_sections", "Evenly distributed XP across Assessment Sections."),
        ("F-02a", "Sub-Skill XP Weight (LO)", "xp_per_LO / num_skills_in_LO", "For multi-skill LOs: XP splits evenly across skills."),
        ("F-02b", "Sub-Skill XP Weight (Section)", "xp_per_section / num_skills_in_section", "For multi-skill Sections: XP splits evenly across skills."),
        ("F-03", "% Score", "actual_score / max_score", "Performance percentage for each skill-row."),
        ("F-04", "Weighted Score", "pct_score × sub_skill_xp_weight", "XP-weighted performance per skill-row."),
        ("F-05", "Average Skill Score", "AVERAGE(all pct_scores for skill)", "Simple average across all courses (FPR + Assessment)."),
        ("F-06", "Avg Skill Weighted XP Score", "SUM(weighted_scores) / SUM(xp_weights)", "Weighted average — higher XP courses matter more."),
    ]:
        st.markdown(f'<div style="margin-bottom:14px"><div class="formula-title">{cid}: {name}</div><div class="formula-desc">{desc}</div><div class="formula-block">{formula}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Reference Tables</div>', unsafe_allow_html=True)
    t1, t2, t3, t4, t5 = st.tabs(["Status", "Category", "Subject", "Multiplier", "Decay"])
    with t1: st.dataframe(pd.DataFrame(STATUS_THRESHOLDS), use_container_width=True, hide_index=True)
    with t2: st.dataframe(pd.DataFrame(CATEGORY_THRESHOLDS), use_container_width=True, hide_index=True)
    with t3: st.dataframe(pd.DataFrame(SUBJECT_THRESHOLDS), use_container_width=True, hide_index=True)
    with t4: st.dataframe(pd.DataFrame(MULTIPLIER_BANDS), use_container_width=True, hide_index=True)
    with t5:
        st.dataframe(pd.DataFrame(DECAY_RATES_ACTIVE), use_container_width=True, hide_index=True)
        st.dataframe(pd.DataFrame(DECAY_RATES_INACTIVE), use_container_width=True, hide_index=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GLOSSARY — XP + FPR/Assessment terms
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def page_glossary():
    st.markdown('<div class="page-title">Glossary</div>', unsafe_allow_html=True)
    for term, defn in [
        ("Course", "A structured learning program with start/end dates, schedule, subjects, and a split method (% or lesson). Assessment is at course level."),
        ("Subject", "Base unit from config. Has predefined category splits. Maps to 6 XP categories."),
        ("Percentage Split (Case 1)", "Subject XP distribution defined as percentages (20% English, 60% Rugby). Each lesson uses course-level shares. XP flows: share × subject's category splits."),
        ("Lesson Split (Case 2)", "Each lesson row has subjects assigned individually. Multi-subject lessons split XP equally. Course-level splits computed from lesson frequencies."),
        ("Subject Shares", "Per-lesson distribution. Case 1: same every lesson from %. Case 2: varies per lesson row. Multi-subject = equal share."),
        ("Weighted Category Splits", "Course-level category %s derived from subject shares × subject category configs. Used for L1 sub-unit computation."),
        ("XP Unit (L2)", "minutes × 0.01 × multiplier."),
        ("XP Sub-Unit (L1)", "L2 adjusted × Σ(subject_share × subject_category_split). Distributes XP across 6 categories."),
        ("Performance Multiplier", "Course-level. 1.0x (0-79%), 1.25x (80-89%), 1.5x (90-100%). Applied from assessment."),
        ("Compound Decay", "Daily reduction. 5 age bands, active vs inactive. Grace period 0-6 months."),
        ("Subject Tracking", "Even with multi-subject lessons, per-subject XP is tracked via shares for subject levels, badges, and insights."),
        ("Final Progress Report (FPR)", "End-of-course evaluation of Learning Objectives on a 1-5 scale. Skills are linked to LOs, not lessons."),
        ("Assessment", "Structured assessment with variable-score Sections. Each Section maps to 1+ skills."),
        ("Learning Objective (LO)", "A unit within a Final Progress Report. Each LO maps to 1+ skills and has a score (1-5)."),
        ("Section", "A unit within an Assessment. Each Section maps to 1+ skills and has a variable max score."),
        ("Skill", "A measurable ability linked to Learning Objectives and Assessment Sections (e.g., Reading, Writing, Speaking)."),
        ("Skill-Row", "An expanded record where each skill in a multi-skill LO/Section becomes its own aggregation row."),
        ("XP Weight (F-01)", "Base XP of a course evenly distributed across LOs (FPR) or Sections (Assessment)."),
        ("Sub-Skill XP Weight (F-02)", "For multi-skill LOs/Sections, XP Weight further splits evenly across skills."),
        ("% Score (F-03)", "actual_score / max_score. Performance percentage per skill-row."),
        ("Weighted Score (F-04)", "% Score × Sub-Skill XP Weight. XP-weighted performance."),
        ("Average Skill Score (F-05)", "Simple average of all % Scores for a skill across all courses."),
        ("Avg Skill Weighted XP Score (F-06)", "SUM(Weighted Scores) / SUM(XP Weights). Heavier courses contribute more."),
        ("Cross-Course Aggregation", "Combining all skill-rows from all courses (FPR + Assessment) to compute F-05 and F-06."),
        ("Base XP", "Course total XP: number_of_lessons × 0.6 (since 1 minute = 0.01 XP, 60-min lesson = 0.6 XP)."),
    ]:
        st.markdown(f'<div style="margin-bottom:8px"><span class="glossary-term">{term}</span><div class="glossary-def">{defn}</div></div>', unsafe_allow_html=True)

# ━━━ ROUTER ━━━
{"mock_data": page_mock_data, "data_dashboard": page_data_dashboard, "calculations": page_calculations,
 "skills_calc": page_skills_calc, "xp_dashboard": page_xp_dashboard, "insights": page_insights,
 "final_report": page_final_report, "formulas": page_formulas, "glossary": page_glossary
}.get(st.session_state.page, page_mock_data)()
