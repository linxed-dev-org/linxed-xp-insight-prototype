"""
Linxed XP System — Calculation Engine
Implements CALC-001 through CALC-018 from XP_Calculation_Framework_Optimized_Guide_V5_2_1.md
11-Level Pipeline: L1 (Sub-Unit) → L11 (Total Decayed)
"""

import json
import math
from datetime import datetime, timedelta
from collections import defaultdict
from config import (
    BASE_XP_RATE, PERF_DEFAULT, RATING_SCALE_MAX,
    MULTIPLIER_BANDS, CATEGORIES, CATEGORY_DISPLAY,
    STATUS_THRESHOLDS, CATEGORY_THRESHOLDS, SUBJECT_THRESHOLDS,
    DECAY_RATES_ACTIVE, DECAY_RATES_INACTIVE,
    INACTIVITY_THRESHOLD, SUBJECT_CATEGORY_CONFIG,
)


class XPCalculationEngine:
    """
    Full XP calculation pipeline.
    Takes raw attendance + assessment data and computes all derived metrics.
    """

    def __init__(self, student, blocks, attendance, assessments, calc_date=None):
        self.student = student
        self.blocks = {b["block_id"]: b for b in blocks}
        self.attendance = sorted(attendance, key=lambda x: x["att_date"])
        self.assessments = {a.get("block_id") or a.get("course_id", ""): a for a in assessments}
        self.calc_date = calc_date or datetime.now().date()
        if isinstance(self.calc_date, datetime):
            self.calc_date = self.calc_date.date()
        self.decay_overrides = None  # set externally to override CFG decay rates

    # ─── CALC-001: XP Unit (L2) ───
    def calc_xp_unit_raw(self, minutes_attended):
        """xp_unit_raw = minutes_attended * 0.01"""
        return round(minutes_attended * BASE_XP_RATE, 12)

    # ─── CALC-005: Performance Multiplier Pipeline ───
    def calc_performance_multiplier(self, skill_ratings):
        """ratings → avg → % → band lookup"""
        if not skill_ratings:
            return PERF_DEFAULT, 0, 0
        avg = round(sum(skill_ratings) / len(skill_ratings), 6)
        pct = round((avg / RATING_SCALE_MAX) * 100, 2)
        mult = PERF_DEFAULT
        for band in MULTIPLIER_BANDS:
            if band["min_pct"] <= pct <= band["max_pct"]:
                mult = band["multiplier"]
                break
        return mult, avg, pct

    # ─── CALC-002: XP Sub-Units (L1) ───
    def calc_sub_units(self, xp_unit_adjusted, subject):
        """Category breakdown at attendance time."""
        cfg = SUBJECT_CATEGORY_CONFIG.get(subject, {})
        sub_units = {}
        for cat in CATEGORIES:
            weight = cfg.get(cat, 0)
            frac = weight / 100.0 if weight > 1 else weight
            sub_units[cat] = round(xp_unit_adjusted * frac, 12)
        return sub_units

    # ─── CALC-007: Compound Daily Decay ───
    def calc_decay_for_sub_unit(self, earned_value, earned_date, category, is_active):
        """Apply compound daily decay to a single XP sub-unit."""
        if isinstance(earned_date, str):
            earned_date = datetime.strptime(earned_date, "%Y-%m-%d").date()

        cur = earned_value
        if cur <= 0:
            return 0.0, 0.0

        d = earned_date + timedelta(days=1)
        while d <= self.calc_date:
            age_days = (d - earned_date).days
            age_months = age_days / 30.44
            rate = self._get_decay_rate(age_months, is_active)
            if rate > 0:
                cur = round(cur * (1.0 - rate), 12)
            d += timedelta(days=1)

        decay_amount = earned_value - cur
        return max(0, round(cur, 12)), round(decay_amount, 12)

    def _get_decay_rate(self, age_months, is_active):
        """Get daily decay rate based on age and activity status. Uses overrides if set."""
        if self.decay_overrides:
            rates = self.decay_overrides.get("active" if is_active else "inactive", [])
        else:
            rates = DECAY_RATES_ACTIVE if is_active else DECAY_RATES_INACTIVE
        for band in rates:
            if band["min_months"] <= age_months < band["max_months"]:
                return band["rate"]
        return rates[-1]["rate"] if rates else 0

    # ─── CALC-010: Category Level ───
    def calc_category_level(self, cat_xp_live):
        """LOOKUP(xp, CFG-006)"""
        for t in reversed(CATEGORY_THRESHOLDS):
            if cat_xp_live >= t["min_xp"]:
                return t["level"]
        return 0

    # ─── CALC-011: Student Status ───
    def calc_student_status(self, total_xp_live):
        """LOOKUP(xp, CFG-005)"""
        for t in reversed(STATUS_THRESHOLDS):
            if total_xp_live >= t["min_xp"]:
                return t["level"], t["name"]
        return 1, "New Learner"

    # ─── CALC-012: Subject Level + Badge ───
    def calc_subject_level(self, subject_xp_live):
        """LOOKUP(xp, CFG-007)"""
        for t in reversed(SUBJECT_THRESHOLDS):
            if subject_xp_live >= t["min_xp"]:
                return t["level"], t.get("badge")
        return 0, None

    # ─── CALC-013: Progress Percentage ───
    def calc_progress_pct(self, current_xp, thresholds, current_level):
        """(xp - min) / (max - min) * 100"""
        for t in thresholds:
            if t.get("level") == current_level:
                min_xp = t["min_xp"]
                max_xp = t["max_xp"]
                if max_xp <= min_xp:
                    return 100.0
                return round(min(100.0, max(0.0, (current_xp - min_xp) / (max_xp - min_xp) * 100)), 2)
        return 0.0

    # ─── CALC-016: Engagement Score ───
    def calc_engagement_score(self, consistency, balance, streak, performance):
        """0.30*cons + 0.25*bal + 0.25*str + 0.20*perf) * 100"""
        return round((0.30 * consistency + 0.25 * balance + 0.25 * streak + 0.20 * performance) * 100, 2)

    # ─── FULL PIPELINE ───
    def compute_all(self):
        """Run the complete 11-level XP pipeline and return comprehensive results."""

        present_att = [a for a in self.attendance if a["att_status"] == "present"]

        # ─── Block-Level Aggregation ───
        block_results = {}
        for blk_id, blk in self.blocks.items():
            blk_att = [a for a in present_att if a["block_id"] == blk_id]
            is_active = bool(blk.get("is_active", 1))
            multiplier = blk.get("performance_multiplier", PERF_DEFAULT)

            # CALC-003: Block Raw Total (L3)
            block_xp_raw = sum(a["xp_unit_raw"] for a in blk_att)

            # CALC-006: Block Total (L5)
            block_xp_adjusted = round(block_xp_raw * multiplier, 12)

            # CALC-004: Block Category Totals (L4)
            block_cat_earned = defaultdict(float)
            block_cat_decayed = defaultdict(float)
            block_cat_live = defaultdict(float)

            total_decay = 0.0
            for a in blk_att:
                su = a.get("sub_units", {})
                if isinstance(su, str):
                    su = json.loads(su)
                for cat in CATEGORIES:
                    earned_val = su.get(cat, 0)
                    # Apply multiplier to get actual earned
                    actual_earned = round(earned_val, 12)
                    block_cat_earned[cat] += actual_earned

                    # CALC-007: Decay per sub-unit
                    live_val, decay_val = self.calc_decay_for_sub_unit(
                        actual_earned,
                        a["att_date"],
                        cat,
                        is_active
                    )
                    block_cat_decayed[cat] += decay_val
                    block_cat_live[cat] += live_val
                    total_decay += decay_val

            block_xp_live = round(block_xp_adjusted - total_decay, 6)
            block_att_count = len(blk_att)
            total_all_att = len([a for a in self.attendance if a["block_id"] == blk_id])
            block_total_mins = sum(a["minutes_attended"] for a in blk_att)
            block_avg_xp = round(block_xp_adjusted / block_att_count, 6) if block_att_count > 0 else 0

            # Assessment info
            asmt = self.assessments.get(blk_id)

            block_results[blk_id] = {
                "block_id": blk_id,
                "subject": blk.get("subject", blk.get("course_name", "")),
                "block_name": blk.get("block_name", ""),
                "is_active": is_active,
                "multiplier": multiplier,
                "assessment_status": blk.get("assessment_status", "pending"),
                "assessment": asmt,
                # L3
                "block_xp_raw": round(block_xp_raw, 6),
                # L5
                "block_xp_adjusted": round(block_xp_adjusted, 6),
                "block_xp_decayed": round(total_decay, 6),
                "block_xp_live": round(block_xp_live, 6),
                # L4
                "block_cat_earned": {c: round(v, 6) for c, v in block_cat_earned.items()},
                "block_cat_decayed": {c: round(v, 6) for c, v in block_cat_decayed.items()},
                "block_cat_live": {c: round(v, 6) for c, v in block_cat_live.items()},
                # Counts
                "att_count_present": block_att_count,
                "att_count_total": total_all_att,
                "total_minutes": block_total_mins,
                "total_hours": round(block_total_mins / 60, 2),
                "avg_xp_per_session": block_avg_xp,
                "lesson_duration": blk.get("lesson_duration", 60),
            }

        # ─── CALC-008: Category Aggregation (L6-L8) ───
        cat_results = {}
        for cat in CATEGORIES:
            cat_earned = sum(br["block_cat_earned"].get(cat, 0) for br in block_results.values())
            cat_decayed = sum(br["block_cat_decayed"].get(cat, 0) for br in block_results.values())
            cat_live = round(cat_earned - cat_decayed, 6)
            cat_level = self.calc_category_level(cat_live)
            cat_pct = self.calc_progress_pct(cat_live, CATEGORY_THRESHOLDS, cat_level)

            cat_sessions = sum(br["att_count_present"] for br in block_results.values()
                             if br["block_cat_earned"].get(cat, 0) > 0)
            cat_hours = sum(br["total_hours"] for br in block_results.values()
                          if br["block_cat_earned"].get(cat, 0) > 0)

            cat_results[cat] = {
                "category": cat,
                "display_name": CATEGORY_DISPLAY.get(cat, cat),
                "cat_xp_earned": round(cat_earned, 6),
                "cat_xp_decayed": round(cat_decayed, 6),
                "cat_xp_live": cat_live,
                "cat_level": cat_level,
                "cat_level_pct": cat_pct,
                "cat_sessions": cat_sessions,
                "cat_hours": round(cat_hours, 2),
                "is_active": cat_live > 0,
            }

        # ─── CALC-009: Student Total (L9-L11) ───
        total_xp_earned = sum(br["block_xp_adjusted"] for br in block_results.values())
        total_xp_decayed = sum(br["block_xp_decayed"] for br in block_results.values())
        total_xp_live = round(total_xp_earned - total_xp_decayed, 6)

        # CALC-011: Student Status
        status_level, status_name = self.calc_student_status(total_xp_live)
        status_pct = self.calc_progress_pct(total_xp_live, STATUS_THRESHOLDS, status_level)

        # Subject-level: distribute each lesson's XP across subjects via subject_shares
        subject_results = {}
        for a in present_att:
            xp_adj = a.get("xp_unit_adjusted", 0)
            # Get subject shares: multi-subject or single-subject
            shares = a.get("subject_shares", {})
            if isinstance(shares, str):
                try: shares = json.loads(shares)
                except: shares = {}
            if not shares:
                # Fallback: try single subject field
                subj = a.get("subject") or a.get("subjects_list", "Unknown")
                if subj and subj != "Unknown":
                    first_subj = subj.split(",")[0].strip()
                    shares = {first_subj: 1.0}
                else:
                    shares = {"Unknown": 1.0}

            # Get course-level multiplier
            cid = a.get("course_id", "")
            course_data = None
            for c in self.blocks.values():
                if c.get("course_id") == cid:
                    course_data = c; break
            is_active = bool(course_data.get("is_active", 1)) if course_data else True

            # Distribute XP to each subject by its share
            su = a.get("sub_units", {})
            if isinstance(su, str):
                try: su = json.loads(su)
                except: su = {}

            att_total_decay = 0.0
            for cat in CATEGORIES:
                ev = su.get(cat, 0)
                if ev > 0:
                    _, dv = self.calc_decay_for_sub_unit(ev, a["att_date"], cat, is_active)
                    att_total_decay += dv

            for subj, share in shares.items():
                subj = subj.strip()
                if subj not in subject_results:
                    subject_results[subj] = {
                        "subject": subj,
                        "xp_earned": 0, "xp_decayed": 0, "xp_live": 0,
                        "sessions": 0, "minutes": 0, "hours": 0,
                    }
                sr = subject_results[subj]
                sr["sessions"] += 1
                sr["minutes"] += round(a["minutes_attended"] * share)
                sr["hours"] = round(sr["minutes"] / 60, 2)
                sr["xp_earned"] += xp_adj * share
                sr["xp_decayed"] += att_total_decay * share
                sr["xp_live"] = round(sr["xp_earned"] - sr["xp_decayed"], 6)

        for subj, sr in subject_results.items():
            sr["xp_earned"] = round(sr["xp_earned"], 6)
            sr["xp_live"] = round(sr["xp_live"], 6)
            level, badge = self.calc_subject_level(sr["xp_live"])
            sr["level"] = level
            sr["badge"] = badge
            sr["level_pct"] = self.calc_progress_pct(sr["xp_live"], SUBJECT_THRESHOLDS, level)

        # ─── CALC-014: Study Hours ───
        total_minutes = sum(a["minutes_attended"] for a in present_att)
        total_hours = round(total_minutes / 60, 2)
        total_sessions = len(present_att)

        # ─── CALC-017: XP Efficiency ───
        xp_efficiency = round(total_xp_earned / total_hours, 4) if total_hours > 0 else 0

        # ─── CALC-015: Improvement Rate ───
        monthly_xp = self._calc_monthly_xp(present_att)
        improvement_rate = None
        if len(monthly_xp) >= 2:
            months = sorted(monthly_xp.keys())
            cur = monthly_xp[months[-1]]
            prev = monthly_xp[months[-2]]
            if prev > 0:
                improvement_rate = round((cur - prev) / prev * 100, 2)

        # ─── CALC-016: Engagement Score ───
        enrollment_date = datetime.strptime(self.student["enrollment_date"][:10], "%Y-%m-%d").date()
        weeks_enrolled = max(1, (self.calc_date - enrollment_date).days / 7)

        # Consistency
        active_weeks = self._count_active_weeks(present_att)
        consistency = min(1.0, active_weeks / weeks_enrolled)

        # Balance
        active_cat_xp = [cr["cat_xp_live"] for cr in cat_results.values() if cr["cat_xp_live"] > 0]
        if len(active_cat_xp) > 1:
            mean_cat = sum(active_cat_xp) / len(active_cat_xp)
            variance = sum((x - mean_cat) ** 2 for x in active_cat_xp) / len(active_cat_xp)
            std_cat = math.sqrt(variance)
            cv = std_cat / mean_cat if mean_cat > 0 else 0
            balance = max(0, 1 - cv)
        else:
            balance = 0.0

        # Streak
        streak_current = self._calc_current_streak(present_att)
        streak = min(1.0, streak_current / 12)

        # Performance
        avg_mult = sum(br["multiplier"] for br in block_results.values()) / max(1, len(block_results))
        perf_norm = (avg_mult - 1.0) / 0.5

        engagement_score = self.calc_engagement_score(consistency, balance, streak, perf_norm)

        # ─── CALC-018: Category XP Velocity ───
        cat_velocity = {}
        cutoff_28d = self.calc_date - timedelta(days=28)
        for cat in CATEGORIES:
            recent_xp = 0
            for a in present_att:
                att_d = datetime.strptime(a["att_date"], "%Y-%m-%d").date()
                if att_d >= cutoff_28d:
                    su = a.get("sub_units", {})
                    if isinstance(su, str):
                        su = json.loads(su)
                    recent_xp += su.get(cat, 0)
            cat_velocity[cat] = round(recent_xp / 4, 6)

        # Decay percentage
        decay_pct = round((total_xp_decayed / total_xp_earned) * 100, 2) if total_xp_earned > 0 else 0

        # Active categories count
        active_cats = sum(1 for cr in cat_results.values() if cr["cat_xp_live"] > 0)

        # Strongest/weakest
        active_cr = [(c, cr["cat_xp_live"]) for c, cr in cat_results.items() if cr["cat_xp_live"] > 0]
        strongest = max(active_cr, key=lambda x: x[1])[0] if active_cr else None
        weakest = min(active_cr, key=lambda x: x[1])[0] if active_cr else None

        # Next status info
        next_status = None
        for t in STATUS_THRESHOLDS:
            if t["level"] == status_level + 1:
                next_status = t
                break

        # ── Course-level aggregation ──
        course_results = {}
        for blk_id, br in block_results.items():
            cid = self.blocks[blk_id].get("course_id", "unknown")
            cname = self.blocks[blk_id].get("course_name") or self.blocks[blk_id].get("block_name", cid)
            if cid not in course_results:
                course_results[cid] = {
                    "course_id": cid, "course_name": cname,
                    "xp_earned": 0, "xp_decayed": 0, "xp_live": 0,
                    "sessions": 0, "minutes": 0, "hours": 0,
                    "blocks": [], "subjects": set(),
                    "cat_earned": defaultdict(float), "cat_live": defaultdict(float),
                }
            cr = course_results[cid]
            cr["xp_earned"] += br["block_xp_adjusted"]
            cr["xp_decayed"] += br["block_xp_decayed"]
            cr["xp_live"] += br["block_xp_live"]
            cr["sessions"] += br["att_count_present"]
            cr["minutes"] += br["total_minutes"]
            cr["hours"] += br["total_hours"]
            cr["blocks"].append(blk_id)
            for cat in CATEGORIES:
                cr["cat_earned"][cat] += br["block_cat_earned"].get(cat, 0)
                cr["cat_live"][cat] += br["block_cat_live"].get(cat, 0)

        # Gather subjects from attendance subject_shares for accurate course→subject mapping
        for a in present_att:
            cid = a.get("course_id", "unknown")
            if cid in course_results:
                shares = a.get("subject_shares", {})
                if isinstance(shares, str):
                    try: shares = json.loads(shares)
                    except: shares = {}
                for subj in shares.keys():
                    s = subj.strip()
                    if s and s != "Unknown":
                        course_results[cid]["subjects"].add(s)

        for cid, cr in course_results.items():
            cr["xp_earned"] = round(cr["xp_earned"], 6)
            cr["xp_live"] = round(cr["xp_live"], 6)
            cr["xp_decayed"] = round(cr["xp_decayed"], 6)
            cr["hours"] = round(cr["hours"], 2)
            cr["subjects"] = sorted(cr["subjects"])
            cr["cat_earned"] = {c: round(v, 6) for c, v in cr["cat_earned"].items()}
            cr["cat_live"] = {c: round(v, 6) for c, v in cr["cat_live"].items()}

        return {
            "student": self.student,
            "calc_date": str(self.calc_date),
            # L9-L11: Student Totals
            "total_xp_earned": round(total_xp_earned, 6),
            "total_xp_decayed": round(total_xp_decayed, 6),
            "total_xp_live": round(total_xp_live, 6),
            # Status
            "status_level": status_level,
            "status_name": status_name,
            "status_pct": status_pct,
            "next_status": next_status,
            # Aggregates
            "total_sessions": total_sessions,
            "total_minutes": total_minutes,
            "total_hours": total_hours,
            "xp_efficiency": xp_efficiency,
            "improvement_rate": improvement_rate,
            "engagement_score": engagement_score,
            "decay_pct": decay_pct,
            # Streaks
            "streak_current": streak_current,
            "streak_longest": streak_current,
            # Category analysis
            "active_cats_count": active_cats,
            "strongest_cat": strongest,
            "weakest_cat": weakest,
            "balance_score": round(balance * 100, 2),
            # Velocity
            "cat_velocity": cat_velocity,
            # Monthly
            "monthly_xp": monthly_xp,
            # Detailed results
            "blocks": block_results,
            "categories": cat_results,
            "subjects": subject_results,
            "courses": course_results,
        }

    def _calc_monthly_xp(self, present_att):
        """Group XP earned by month."""
        monthly = defaultdict(float)
        for a in present_att:
            month_key = a["att_date"][:7]
            monthly[month_key] += a["xp_unit_adjusted"]
        return {k: round(v, 6) for k, v in sorted(monthly.items())}

    def _count_active_weeks(self, present_att):
        """Count distinct weeks with at least one attendance."""
        weeks = set()
        for a in present_att:
            d = datetime.strptime(a["att_date"], "%Y-%m-%d").date()
            week_num = d.isocalendar()[1]
            year = d.year
            weeks.add((year, week_num))
        return len(weeks)

    def _calc_current_streak(self, present_att):
        """Count consecutive weeks with attendance going back from most recent attendance."""
        if not present_att:
            return 0
        weeks_with_att = set()
        latest_date = None
        for a in present_att:
            d = datetime.strptime(a["att_date"], "%Y-%m-%d").date()
            iso = d.isocalendar()
            weeks_with_att.add((iso[0], iso[1]))
            if latest_date is None or d > latest_date:
                latest_date = d
        if not latest_date:
            return 0
        streak = 0
        check_date = latest_date
        while True:
            iso = check_date.isocalendar()
            if (iso[0], iso[1]) in weeks_with_att:
                streak += 1
                check_date -= timedelta(weeks=1)
            else:
                break
        return streak
