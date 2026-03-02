"""
Linxed XP v4.0 — Skills Calculation Engine
Implements Oliver's FPR/Assessment Calculation Framework (25 Feb Meeting)
Formulas F-01 through F-06 from Linxed_Finalized_Calculation_Framework_27_feb.xlsx

Key Insight: FPR Learning Objectives and Assessment Sections are both just
"skill-rows" in the final aggregation. F-05 and F-06 consume pct_score and
xp_weight uniformly — regardless of whether the source is FPR or Assessment.
"""
from collections import defaultdict


def parse_skill_categories(skill_str):
    """Parse skill category string into list of individual skills.
    Handles separators: ' and ', ' & ', ','
    """
    if isinstance(skill_str, list):
        return skill_str
    if not skill_str:
        return []
    # Normalize separators
    s = skill_str.replace(" & ", " and ").replace(",", " and ")
    parts = [p.strip() for p in s.split(" and ") if p.strip()]
    return parts


def compute_course_skill_rows(fpr_los, asmt_sections):
    """
    Compute expanded skill-rows for a single course.
    Each LO/Section with N skills produces N skill-rows.

    Returns list of dicts:
    [{
        "source": "FPR" | "Assessment",
        "source_name": "LO-1" | "Section 1",
        "skill": "Reading",
        "xp_weight": float,  # F-02a/b: sub-skill weight
        "max_score": float,
        "actual_score": float,
        "pct_score": float,   # F-03
        "weighted_score": float,  # F-04
    }]
    """
    rows = []

    for lo in fpr_los:
        skills = lo.get("skills", [])
        if isinstance(skills, str):
            import json
            try: skills = json.loads(skills)
            except: skills = [skills]
        for skill in skills:
            rows.append({
                "source": "FPR",
                "source_name": lo.get("lo_name", f"LO-{lo.get('lo_index',0)}"),
                "skill": skill,
                "xp_weight": lo.get("xp_weight", 0),
                "max_score": lo.get("max_score", 5),
                "actual_score": lo.get("actual_score", 0),
                "pct_score": lo.get("pct_score", 0),
                "weighted_score": lo.get("weighted_score", 0),
            })

    for sec in asmt_sections:
        skills = sec.get("skills", [])
        if isinstance(skills, str):
            import json
            try: skills = json.loads(skills)
            except: skills = [skills]
        for skill in skills:
            rows.append({
                "source": "Assessment",
                "source_name": sec.get("section_name", f"Section {sec.get('section_index',0)}"),
                "skill": skill,
                "xp_weight": sec.get("xp_weight", 0),
                "max_score": sec.get("max_score", 5),
                "actual_score": sec.get("actual_score", 0),
                "pct_score": sec.get("pct_score", 0),
                "weighted_score": sec.get("weighted_score", 0),
            })

    return rows


def compute_course_skill_aggregate(skill_rows):
    """
    Aggregate skill metrics at the course level.
    Returns dict: {skill: {"xp_weight": float, "avg_pct": float, "count": int}}
    """
    skill_data = defaultdict(lambda: {"pct_scores": [], "xp_weights": [], "weighted_scores": []})
    for r in skill_rows:
        sk = r["skill"]
        skill_data[sk]["pct_scores"].append(r["pct_score"])
        skill_data[sk]["xp_weights"].append(r["xp_weight"])
        skill_data[sk]["weighted_scores"].append(r["weighted_score"])

    result = {}
    for sk, data in skill_data.items():
        total_xp = sum(data["xp_weights"])
        total_weighted = sum(data["weighted_scores"])
        avg_pct = sum(data["pct_scores"]) / len(data["pct_scores"]) if data["pct_scores"] else 0
        result[sk] = {
            "total_xp_weight": round(total_xp, 6),
            "total_weighted_score": round(total_weighted, 6),
            "avg_pct_score": round(avg_pct, 6),
            "count": len(data["pct_scores"]),
        }
    return result


def compute_cross_course_aggregation(all_course_skill_rows):
    """
    Cross-course aggregation: combine all skill-rows from all courses.

    all_course_skill_rows: list of dicts with keys:
        course_name, source, source_name, skill, xp_weight, pct_score, weighted_score

    Returns:
        cross_rows: flat list for the cross-course table
        final_output: dict per skill with F-05 and F-06
    """
    cross_rows = []
    skill_data = defaultdict(lambda: {"pct_scores": [], "xp_weights": [], "weighted_scores": []})

    for r in all_course_skill_rows:
        cross_rows.append(r)
        sk = r["skill"]
        skill_data[sk]["pct_scores"].append(r["pct_score"])
        skill_data[sk]["xp_weights"].append(r["xp_weight"])
        skill_data[sk]["weighted_scores"].append(r["weighted_score"])

    final_output = {}
    for sk, data in skill_data.items():
        n = len(data["pct_scores"])
        # F-05: Average Skill Score = AVERAGE(all pct_scores for that skill)
        avg_skill_score = round(sum(data["pct_scores"]) / n, 6) if n > 0 else 0
        # F-06: Avg Skill Weighted XP Score = SUM(weighted) / SUM(xp_weights)
        total_xp = sum(data["xp_weights"])
        total_weighted = sum(data["weighted_scores"])
        avg_wtd_xp_score = round(total_weighted / total_xp, 6) if total_xp > 0 else 0
        final_output[sk] = {
            "skill": sk,
            "avg_skill_score": avg_skill_score,           # F-05
            "avg_skill_wtd_xp_score": avg_wtd_xp_score,   # F-06
            "total_xp_weight": round(total_xp, 6),
            "total_weighted_score": round(total_weighted, 6),
            "count": n,
        }

    return cross_rows, final_output


def compute_full_skills_pipeline(student_fpr_los, student_asmt_sections, courses):
    """
    Full skills calculation pipeline for a student.

    Args:
        student_fpr_los: all FPR LO records for the student
        student_asmt_sections: all Assessment section records for the student
        courses: course records for course metadata

    Returns dict with:
        per_course: {course_id: {course_name, base_xp, skill_rows, skill_aggregate}}
        cross_course_rows: flat list for cross-course table
        final_output: {skill: {F-05, F-06, totals}}
    """
    course_map = {c["course_id"]: c for c in courses}

    # Group FPR/Assessment records by course
    fpr_by_course = defaultdict(list)
    asmt_by_course = defaultdict(list)
    for lo in student_fpr_los:
        fpr_by_course[lo["course_id"]].append(lo)
    for sec in student_asmt_sections:
        asmt_by_course[sec["course_id"]].append(sec)

    per_course = {}
    all_cross_rows = []

    # Process each course that has FPR or Assessment
    all_course_ids = set(list(fpr_by_course.keys()) + list(asmt_by_course.keys()))
    for cid in all_course_ids:
        c = course_map.get(cid, {})
        cname = c.get("course_name", "Unknown Course")
        num_lessons = c.get("num_lessons", 0)
        base_xp = round(num_lessons * 0.6, 6)

        fpr_los = fpr_by_course.get(cid, [])
        asmt_secs = asmt_by_course.get(cid, [])

        skill_rows = compute_course_skill_rows(fpr_los, asmt_secs)
        skill_agg = compute_course_skill_aggregate(skill_rows)

        per_course[cid] = {
            "course_id": cid,
            "course_name": cname,
            "base_xp": base_xp,
            "num_lessons": num_lessons,
            "has_fpr": len(fpr_los) > 0,
            "has_assessment": len(asmt_secs) > 0,
            "fpr_los": fpr_los,
            "asmt_sections": asmt_secs,
            "skill_rows": skill_rows,
            "skill_aggregate": skill_agg,
        }

        # Add to cross-course with course context
        for r in skill_rows:
            all_cross_rows.append({
                "course_name": cname,
                "course_id": cid,
                **r,
            })

    cross_rows, final_output = compute_cross_course_aggregation(all_cross_rows)

    return {
        "per_course": per_course,
        "cross_course_rows": cross_rows,
        "final_output": final_output,
    }
