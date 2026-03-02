"""
Linxed XP v3.0 — Configuration
Aligned with 23 Feb meeting: subjects are base units, no predefined courses in UI.
"""

BASE_XP_RATE = 0.01
PERF_DEFAULT = 1.0
RATING_SCALE_MAX = 5

MULTIPLIER_BANDS = [
    {"min_pct": 0, "max_pct": 79.99, "multiplier": 1.0, "label": "Standard"},
    {"min_pct": 80, "max_pct": 89.99, "multiplier": 1.25, "label": "Above Expectations"},
    {"min_pct": 90, "max_pct": 100, "multiplier": 1.5, "label": "Exceptional"},
]

INACTIVITY_THRESHOLD = 183

DECAY_RATES_ACTIVE = [
    {"min_months": 0, "max_months": 6, "rate": 0.0, "label": "0-6 months (grace)"},
    {"min_months": 6, "max_months": 12, "rate": 0.0, "label": "6-12 months"},
    {"min_months": 12, "max_months": 24, "rate": 0.00015, "label": "12-24 months"},
    {"min_months": 24, "max_months": 48, "rate": 0.00025, "label": "24-48 months"},
    {"min_months": 48, "max_months": 9999, "rate": 0.00035, "label": "48+ months"},
]
DECAY_RATES_INACTIVE = [
    {"min_months": 0, "max_months": 6, "rate": 0.0, "label": "0-6 months (grace)"},
    {"min_months": 6, "max_months": 12, "rate": 0.00010, "label": "6-12 months"},
    {"min_months": 12, "max_months": 24, "rate": 0.00020, "label": "12-24 months"},
    {"min_months": 24, "max_months": 48, "rate": 0.00030, "label": "24-48 months"},
    {"min_months": 48, "max_months": 9999, "rate": 0.00040, "label": "48+ months"},
]

STATUS_THRESHOLDS = [
    {"level": 1, "name": "New Learner", "min_xp": 0, "max_xp": 30.0},
    {"level": 2, "name": "Curious Learner", "min_xp": 30.01, "max_xp": 67.51},
    {"level": 3, "name": "Skilled Learner", "min_xp": 67.52, "max_xp": 114.395},
    {"level": 4, "name": "Dedicated Learner", "min_xp": 114.396, "max_xp": 173.0},
    {"level": 5, "name": "Advanced Learner", "min_xp": 173.001, "max_xp": 246.25},
    {"level": 6, "name": "High Achiever", "min_xp": 246.251, "max_xp": 337.81},
    {"level": 7, "name": "Elite Learner", "min_xp": 337.811, "max_xp": 452.26},
    {"level": 8, "name": "Star Student", "min_xp": 452.261, "max_xp": 99999},
]
CATEGORY_THRESHOLDS = [
    {"level": 0, "name": "Unranked", "min_xp": 0, "max_xp": 3.0},
    {"level": 1, "name": "Beginner", "min_xp": 3.01, "max_xp": 10.0},
    {"level": 2, "name": "Developing", "min_xp": 10.01, "max_xp": 25.0},
    {"level": 3, "name": "Proficient", "min_xp": 25.01, "max_xp": 50.0},
    {"level": 4, "name": "Advanced", "min_xp": 50.01, "max_xp": 85.0},
    {"level": 5, "name": "Expert", "min_xp": 85.01, "max_xp": 99999},
]
SUBJECT_THRESHOLDS = [
    {"level":i,"badge":"Bronze" if 5<=i<=10 else ("Silver" if 11<=i<=20 else ("Gold" if i>20 else None)),
     "min_xp":round(0.3*(1.15**i),2),"max_xp":round(0.3*(1.15**(i+1)),2)}
    for i in range(31)
]

CATEGORIES = ["Academic", "Health_Fitness", "Music", "Games_Strategy", "Arts_Creative", "Social"]
CATEGORY_DISPLAY = {
    "Academic": "Academic", "Health_Fitness": "Health & Fitness", "Music": "Music",
    "Games_Strategy": "Games & Strategy", "Arts_Creative": "Arts & Creative", "Social": "Social",
}
LESSON_DURATIONS = [30, 45, 60, 90]
DAYS_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

BRANCHES = [
    {"id": "br_hk_babington", "name": "Babington, Hong Kong"},
    {"id": "br_hk_central", "name": "Central, Hong Kong"},
    {"id": "br_uk_london", "name": "London, UK"},
    {"id": "br_sg_orchard", "name": "Orchard, Singapore"},
]

# ── Subject Category Config — aligned with groups-subjects-skills.xlsx ──
SUBJECT_CATEGORY_CONFIG = {
    # Academic > Language
    "English": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Spanish": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "German": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Mandarin": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "French": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    # Academic > STEM
    "Mathematics": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Chemistry": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Physics": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Biology": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Psychology": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Sociology": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Computer Science": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Science": {"sub_category": "STEM", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    # Academic > Other Subjects
    "History": {"sub_category": "Other Subjects", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Geography": {"sub_category": "Other Subjects", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Economics": {"sub_category": "Other Subjects", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Business": {"sub_category": "Other Subjects", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    # Kept for backward compat with existing v3 profiles
    "Reading": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Writing": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Phonics": {"sub_category": "Language", "Academic": 100, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    # Health & Fitness > Sports
    "Football": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Rugby": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Hockey": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Tennis": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 30, "Arts_Creative": 0, "Social": 10},
    "Table Tennis": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 30, "Arts_Creative": 0, "Social": 10},
    "Golf": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 30, "Arts_Creative": 0, "Social": 10},
    "Netball": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Baseball": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Basketball": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Badminton": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 30, "Arts_Creative": 0, "Social": 10},
    "Fencing": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 30, "Arts_Creative": 0, "Social": 10},
    "Equestrian": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 30, "Arts_Creative": 0, "Social": 10},
    "Figure Skating": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 30, "Arts_Creative": 0, "Social": 10},
    "Cheerleading": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 40},
    "Bowling": {"sub_category": "Sports", "Academic": 0, "Health_Fitness": 20, "Music": 0, "Games_Strategy": 40, "Arts_Creative": 0, "Social": 40},
    # Health & Fitness > Athletics
    "Running": {"sub_category": "Athletics", "Academic": 0, "Health_Fitness": 90, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 10},
    "Cycling": {"sub_category": "Athletics", "Academic": 0, "Health_Fitness": 90, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 10},
    "Climbing": {"sub_category": "Athletics", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Jumping": {"sub_category": "Athletics", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Throwing": {"sub_category": "Athletics", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Gymnastics": {"sub_category": "Athletics", "Academic": 0, "Health_Fitness": 70, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    # Health & Fitness > Dance
    "Ballet": {"sub_category": "Dance", "Academic": 0, "Health_Fitness": 30, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 50, "Social": 20},
    "KPOP": {"sub_category": "Dance", "Academic": 0, "Health_Fitness": 30, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 50, "Social": 20},
    "Hip Hop": {"sub_category": "Dance", "Academic": 0, "Health_Fitness": 30, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 50, "Social": 20},
    "Jazz": {"sub_category": "Dance", "Academic": 0, "Health_Fitness": 30, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 50, "Social": 20},
    "Pop Dance": {"sub_category": "Dance", "Academic": 0, "Health_Fitness": 30, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 50, "Social": 20},
    "Contemporary Dance": {"sub_category": "Dance", "Academic": 0, "Health_Fitness": 30, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 50, "Social": 20},
    "Dance Fitness": {"sub_category": "Dance", "Academic": 0, "Health_Fitness": 30, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 50, "Social": 20},
    # Health & Fitness > General Fitness
    "Weight Training": {"sub_category": "General Fitness", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Crossfit": {"sub_category": "General Fitness", "Academic": 0, "Health_Fitness": 90, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 10},
    "HIT Training": {"sub_category": "General Fitness", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    # Health & Fitness > Water Sports
    "Swimming": {"sub_category": "Water Sports", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Dragon Boating": {"sub_category": "Water Sports", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 40},
    "Surfing": {"sub_category": "Water Sports", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Sailing": {"sub_category": "Water Sports", "Academic": 0, "Health_Fitness": 80, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 20},
    # Health & Fitness > Martial Arts
    "Judo": {"sub_category": "Martial Arts", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Taekwondo": {"sub_category": "Martial Arts", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Jujutsu": {"sub_category": "Martial Arts", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Muay Thai": {"sub_category": "Martial Arts", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Boxing": {"sub_category": "Martial Arts", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Karate": {"sub_category": "Martial Arts", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    "Martial Arts": {"sub_category": "Martial Arts", "Academic": 0, "Health_Fitness": 60, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 20},
    # Health & Fitness > Other
    "Yoga": {"sub_category": "Other", "Academic": 0, "Health_Fitness": 90, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 10},
    "Calisthenics": {"sub_category": "Other", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    "Pilates": {"sub_category": "Other", "Academic": 0, "Health_Fitness": 100, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    # Music > Vocal
    "Choir": {"sub_category": "Vocal", "Academic": 0, "Health_Fitness": 0, "Music": 60, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 20},
    "Singing": {"sub_category": "Vocal", "Academic": 0, "Health_Fitness": 0, "Music": 60, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 20},
    # Music > Instrument
    "Piano": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Violin": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Guitar": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Trumpet": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Cello": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Drums": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Flute": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Clarinet": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Saxophone": {"sub_category": "Instrument", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    # Music > Digital
    "DJing": {"sub_category": "Digital Music", "Academic": 0, "Health_Fitness": 0, "Music": 70, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 10},
    "Music Theory": {"sub_category": "Theory", "Academic": 20, "Health_Fitness": 0, "Music": 80, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 0},
    # Arts & Creative > Visual Arts
    "Arts & Crafts": {"sub_category": "Visual Arts", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 100, "Social": 0},
    "Painting": {"sub_category": "Visual Arts", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 100, "Social": 0},
    "Photography": {"sub_category": "Visual Arts", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 100, "Social": 0},
    "Drawing": {"sub_category": "Visual Arts", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 100, "Social": 0},
    "Digital Art": {"sub_category": "Visual Arts", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 100, "Social": 0},
    "Sculpture": {"sub_category": "Visual Arts", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 100, "Social": 0},
    # Arts & Creative > Drama
    "Acting": {"sub_category": "Drama", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 60, "Social": 40},
    "Musical Theatre": {"sub_category": "Drama", "Academic": 0, "Health_Fitness": 0, "Music": 50, "Games_Strategy": 0, "Arts_Creative": 30, "Social": 20},
    "Drama": {"sub_category": "Drama", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 60, "Social": 40},
    # Games & Strategy
    "Chess": {"sub_category": "Board Games", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 90, "Arts_Creative": 0, "Social": 10},
    "Checkers": {"sub_category": "Board Games", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 90, "Arts_Creative": 0, "Social": 10},
    "Board Games": {"sub_category": "Board Games", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 90, "Arts_Creative": 0, "Social": 10},
    "Poker": {"sub_category": "Card Games", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 70, "Arts_Creative": 0, "Social": 30},
    "Cribbage": {"sub_category": "Card Games", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 70, "Arts_Creative": 0, "Social": 30},
    "Bridge": {"sub_category": "Card Games", "Academic": 0, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 70, "Arts_Creative": 0, "Social": 30},
    "Coding": {"sub_category": "Technology", "Academic": 30, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 60, "Arts_Creative": 0, "Social": 10},
    "Robotics": {"sub_category": "Technology", "Academic": 20, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 50, "Arts_Creative": 20, "Social": 10},
    # Social
    "Playgroup": {"sub_category": "Social Clubs", "Academic": 0, "Health_Fitness": 10, "Music": 10, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 60},
    "Youth Club": {"sub_category": "Social Clubs", "Academic": 0, "Health_Fitness": 10, "Music": 10, "Games_Strategy": 0, "Arts_Creative": 20, "Social": 60},
    # Kept for backward compat
    "Creative Writing": {"sub_category": "Language Arts", "Academic": 30, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 60, "Social": 10},
    "Public Speaking": {"sub_category": "Communication", "Academic": 20, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 10, "Social": 70},
    "Debate": {"sub_category": "Communication", "Academic": 30, "Health_Fitness": 0, "Music": 0, "Games_Strategy": 20, "Arts_Creative": 0, "Social": 50},
    "Team Building": {"sub_category": "Leadership", "Academic": 0, "Health_Fitness": 20, "Music": 0, "Games_Strategy": 10, "Arts_Creative": 0, "Social": 70},
    "Community Service": {"sub_category": "Civic", "Academic": 10, "Health_Fitness": 10, "Music": 0, "Games_Strategy": 0, "Arts_Creative": 0, "Social": 80},
}

# ── Subject Skills — aligned with groups-subjects-skills.xlsx + Babington ──
SUBJECT_SKILLS = {
    # ═══ ACADEMIC > LANGUAGES ═══
    # English has Babington-sourced skills (Reading, Writing, Speaking, Listening, etc.)
    # These are the SAME skills used in Babington FPR/Assessment data
    "English": ["Reading", "Writing", "Speaking", "Listening", "Comprehension", "Spelling", "Grammar", "Behaviour", "Linguistics"],
    "Spanish": ["Reading", "Writing", "Speaking", "Listening", "Comprehension", "Grammar"],
    "German": ["Reading", "Writing", "Speaking", "Listening", "Comprehension", "Grammar"],
    "Mandarin": ["Reading", "Writing", "Speaking", "Listening", "Comprehension", "Grammar"],
    "French": ["Reading", "Writing", "Speaking", "Listening", "Comprehension", "Grammar"],
    # ═══ ACADEMIC > STEM ═══
    "Mathematics": ["Arithmetic", "Algebra", "Geometry", "Statistics", "Problem Solving"],
    "Science": ["Observation", "Hypothesis", "Experimentation", "Analysis", "Critical Thinking"],
    "Chemistry": ["Lab Skills", "Chemical Analysis", "Equations", "Safety"],
    "Physics": ["Mechanics", "Energy", "Experimentation", "Problem Solving"],
    "Biology": ["Observation", "Classification", "Lab Skills", "Analysis"],
    "Computer Science": ["Logic", "Algorithms", "Syntax", "Debugging"],
    # ═══ ACADEMIC > HUMANITIES ═══
    "History": ["Research", "Analysis", "Essay Writing", "Critical Thinking"],
    "Geography": ["Map Skills", "Data Analysis", "Fieldwork", "Research"],
    "Psychology": ["Research Methods", "Analysis", "Critical Thinking", "Essay Writing"],
    "Sociology": ["Research Methods", "Analysis", "Critical Thinking", "Essay Writing"],
    "Economics": ["Data Analysis", "Modelling", "Critical Thinking", "Problem Solving"],
    "Business": ["Planning", "Communication", "Analysis", "Presentation"],
    # ═══ ACADEMIC > LITERACY ═══
    "Reading": ["Decoding", "Fluency", "Comprehension", "Vocabulary"],
    "Writing": ["Handwriting", "Composition", "Grammar", "Spelling"],
    "Phonics": ["Letter Sounds", "Blending", "Segmenting", "Decoding"],
    "Creative Writing": ["Narrative", "Description", "Dialogue", "Creativity"],
    "Public Speaking": ["Confidence", "Clarity", "Persuasion", "Delivery"],
    "Debate": ["Argumentation", "Rebuttal", "Research", "Delivery"],
    # ═══ HEALTH & FITNESS > BALL SPORTS ═══
    "Football": ["Passing", "Shooting", "Tackling", "Dribbling"],
    "Rugby": ["Passing", "Tackling", "Rucking", "Kicking"],
    "Hockey": ["Passing", "Shooting", "Tackling", "Dribbling"],
    "Tennis": ["Serving", "Forehand", "Backhand", "Footwork"],
    "Basketball": ["Shooting", "Dribbling", "Passing", "Defense"],
    "Badminton": ["Serving", "Smash", "Footwork", "Net Play"],
    "Table Tennis": ["Serving", "Spin", "Footwork", "Rally"],
    "Baseball": ["Batting", "Throwing", "Catching", "Base Running"],
    "Netball": ["Passing", "Shooting", "Footwork", "Defense"],
    "Bowling": ["Aim", "Technique", "Consistency", "Strategy"],
    "Golf": ["Driving", "Putting", "Chipping", "Course Management"],
    "Volleyball": ["Serving", "Setting", "Spiking", "Blocking"],
    "Cricket": ["Batting", "Bowling", "Fielding", "Strategy"],
    # ═══ HEALTH & FITNESS > ATHLETICS ═══
    "Running": ["Endurance", "Sprint", "Pace", "Form"],
    "Swimming": ["Freestyle", "Backstroke", "Breaststroke", "Endurance"],
    "Gymnastics": ["Balance", "Flexibility", "Strength", "Coordination"],
    "Cycling": ["Endurance", "Speed", "Hill Climbing", "Technique"],
    "Jumping": ["Technique", "Power", "Coordination", "Landing"],
    "Throwing": ["Technique", "Power", "Aim", "Coordination"],
    # ═══ HEALTH & FITNESS > MARTIAL ARTS ═══
    "Martial Arts": ["Striking", "Defense", "Kata", "Discipline"],
    "Karate": ["Kata", "Kumite", "Blocks", "Discipline"],
    "Judo": ["Throws", "Groundwork", "Balance", "Discipline"],
    "Jujutsu": ["Grappling", "Locks", "Throws", "Discipline"],
    "Taekwondo": ["Kicks", "Forms", "Sparring", "Discipline"],
    "Muay Thai": ["Strikes", "Clinch", "Defense", "Conditioning"],
    "Fencing": ["Footwork", "Blade Work", "Tactics", "Timing"],
    "Boxing": ["Jab", "Defense", "Footwork", "Conditioning"],
    # ═══ HEALTH & FITNESS > DANCE ═══
    "Ballet": ["Posture", "Technique", "Flexibility", "Expression"],
    "Contemporary Dance": ["Fluidity", "Expression", "Technique", "Improvisation"],
    "Hip Hop": ["Rhythm", "Isolation", "Freestyle", "Coordination"],
    "Pop Dance": ["Rhythm", "Coordination", "Performance", "Choreography"],
    "KPOP": ["Rhythm", "Synchronization", "Performance", "Choreography"],
    "Dance Fitness": ["Endurance", "Rhythm", "Coordination", "Flexibility"],
    "Jazz": ["Technique", "Rhythm", "Flexibility", "Performance"],
    "Figure Skating": ["Balance", "Jumps", "Spins", "Expression"],
    "Cheerleading": ["Stunts", "Tumbling", "Coordination", "Performance"],
    # ═══ HEALTH & FITNESS > FITNESS ═══
    "Yoga": ["Flexibility", "Balance", "Breathing", "Mindfulness"],
    "Pilates": ["Core Strength", "Flexibility", "Posture", "Control"],
    "Crossfit": ["Strength", "Endurance", "Speed", "Power"],
    "HIT Training": ["Intensity", "Endurance", "Power", "Recovery"],
    "Weight Training": ["Strength", "Form", "Progressive Load", "Endurance"],
    "Calisthenics": ["Body Control", "Strength", "Flexibility", "Balance"],
    "Climbing": ["Grip Strength", "Technique", "Problem Solving", "Endurance"],
    # ═══ HEALTH & FITNESS > WATER/OUTDOOR ═══
    "Sailing": ["Navigation", "Rope Work", "Wind Reading", "Teamwork"],
    "Surfing": ["Balance", "Paddle", "Wave Reading", "Pop Up"],
    "Dragon Boating": ["Stroke Technique", "Timing", "Endurance", "Teamwork"],
    "Equestrian": ["Riding", "Grooming", "Balance", "Communication"],
    # ═══ MUSIC ═══
    "Piano": ["Sight Reading", "Technique", "Rhythm", "Expression"],
    "Guitar": ["Chord Knowledge", "Strumming", "Picking", "Rhythm"],
    "Violin": ["Bowing", "Intonation", "Sight Reading", "Expression"],
    "Drums": ["Rhythm", "Timing", "Rudiments", "Coordination"],
    "Singing": ["Pitch", "Breath Control", "Tone", "Diction"],
    "Choir": ["Harmony", "Pitch", "Blend", "Sight Reading"],
    "Cello": ["Bowing", "Intonation", "Sight Reading", "Expression"],
    "Flute": ["Embouchure", "Breath Control", "Fingering", "Tone"],
    "Clarinet": ["Embouchure", "Breath Control", "Fingering", "Tone"],
    "Trumpet": ["Embouchure", "Breath Control", "Range", "Tone"],
    "Saxophone": ["Embouchure", "Breath Control", "Fingering", "Improvisation"],
    "DJing": ["Beat Matching", "Mixing", "Track Selection", "Creativity"],
    "Music Theory": ["Notation", "Harmony", "Rhythm", "Ear Training"],
    "Musical Theatre": ["Singing", "Acting", "Dance", "Expression"],
    # ═══ ARTS & CREATIVE ═══
    "Painting": ["Color Theory", "Composition", "Technique", "Creativity"],
    "Drawing": ["Line Work", "Shading", "Perspective", "Composition"],
    "Photography": ["Composition", "Lighting", "Editing", "Creativity"],
    "Drama": ["Expression", "Improvisation", "Voice Projection", "Characterisation"],
    "Acting": ["Characterisation", "Voice Projection", "Movement", "Improvisation"],
    "Sculpture": ["Form", "Material Handling", "Creativity", "Technique"],
    "Digital Art": ["Software Skills", "Composition", "Color Theory", "Creativity"],
    "Arts & Crafts": ["Creativity", "Fine Motor Skills", "Design", "Technique"],
    # ═══ GAMES & STRATEGY ═══
    "Chess": ["Opening Theory", "Tactics", "Endgame", "Strategy"],
    "Checkers": ["Tactics", "Pattern Recognition", "Strategy", "Planning"],
    "Poker": ["Probability", "Bluffing", "Strategy", "Risk Assessment"],
    "Board Games": ["Strategy", "Problem Solving", "Planning", "Critical Thinking"],
    "Bridge": ["Bidding", "Card Play", "Strategy", "Communication"],
    "Cribbage": ["Counting", "Strategy", "Probability", "Hand Management"],
    "Coding": ["Logic", "Syntax", "Problem Solving", "Debugging"],
    "Robotics": ["Design", "Programming", "Mechanics", "Problem Solving"],
    # ═══ SOCIAL ═══
    "Playgroup": ["Sharing", "Communication", "Social Skills", "Cooperation"],
    "Youth Club": ["Leadership", "Teamwork", "Communication", "Social Skills"],
    "Team Building": ["Leadership", "Communication", "Problem Solving", "Cooperation"],
    "Community Service": ["Empathy", "Organisation", "Teamwork", "Communication"],
}

def get_subject_splits(subject):
    """Get normalized category splits for a subject (0-1)."""
    cfg = SUBJECT_CATEGORY_CONFIG.get(subject, {})
    return {cat: cfg.get(cat, 0) / 100.0 for cat in CATEGORIES}

def calc_weighted_category_splits(subject_pcts):
    """
    Calculate weighted category splits from subject percentage splits.
    subject_pcts: dict of {subject_name: percentage} (must sum to ~100)
    Returns: dict of {category: percentage} summing to ~100
    """
    result = {cat: 0.0 for cat in CATEGORIES}
    total_pct = sum(subject_pcts.values()) or 100
    for subj, pct in subject_pcts.items():
        w = pct / total_pct
        cfg = SUBJECT_CATEGORY_CONFIG.get(subj, {})
        for cat in CATEGORIES:
            result[cat] += cfg.get(cat, 0) * w
    return {cat: round(v, 2) for cat, v in result.items()}

def calc_lesson_subject_shares(subjects_in_lesson):
    """
    For a single lesson with multiple subjects, return equal shares.
    subjects_in_lesson: list of subject names
    Returns: dict of {subject: share} where shares sum to 1.0
    """
    n = len(subjects_in_lesson) or 1
    return {s: round(1.0 / n, 6) for s in subjects_in_lesson}

def calc_lesson_category_splits(subject_shares):
    """
    Calculate blended category splits for a lesson based on subject shares.
    subject_shares: dict of {subject: share_fraction}
    Returns: dict of {category: fraction} summing to ~1.0
    """
    result = {cat: 0.0 for cat in CATEGORIES}
    for subj, share in subject_shares.items():
        cfg = SUBJECT_CATEGORY_CONFIG.get(subj, {})
        for cat in CATEGORIES:
            result[cat] += (cfg.get(cat, 0) / 100.0) * share
    return {cat: round(v, 6) for cat, v in result.items()}

def get_multiplier_from_grade(grade_pct):
    for band in MULTIPLIER_BANDS:
        if band["min_pct"] <= grade_pct <= band["max_pct"]:
            return band["multiplier"]
    return PERF_DEFAULT

# ── DEMO PROFILES (used indirectly for initial launch data) ──
# Now includes FPR (Learning Objectives) and Assessment (Sections) definitions
# KEY DESIGN PRINCIPLE: Skills must appear across multiple courses with DIFFERENT
# lesson counts to create meaningful F-05 vs F-06 divergence.
# F-05 = simple average (treats a 10-lesson course same as 50-lesson)
# F-06 = weighted average (50-lesson course weighs 5x more)
# So: same skill, different course sizes, different scores = divergence.

DEMO_PROFILES = [
    # ═══ PROFILE 1: Sarah Chen — Language & Arts focus ═══
    # Reading/Writing/Speaking appear in 3 courses with 38/36/16 lessons
    {
        "name": "Sarah Chen", "dob": "2015-03-15", "enrollment": "2022-09-01", "branch": "br_hk_babington",
        "courses": [
            {"name": "English Ladder - S3M1", "start": "2022-09-05", "end": "2023-06-20", "lessons": 38, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 60, "Reading": 20, "Writing": 20}, "grade": 88,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Vocabulary Development", "skills": ["Reading"]},
                 {"name": "LO-2: Sentence Construction", "skills": ["Writing"]},
                 {"name": "LO-3: Oral Communication", "skills": ["Speaking"]},
                 {"name": "LO-4: Reading Fluency", "skills": ["Reading", "Comprehension"]},
             ], "max_score": 5}},
            {"name": "RWI - F1", "start": "2023-01-10", "end": "2023-12-15", "lessons": 36, "days": ["Wednesday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": None,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Phonics Sounds", "skills": ["Reading", "Spelling"]},
                 {"name": "LO-2: Blending", "skills": ["Reading"]},
                 {"name": "LO-3: Letter Formation", "skills": ["Writing"]},
                 {"name": "LO-4: Story Telling", "skills": ["Speaking", "Listening"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Say The Sounds", "skills": ["Reading", "Speaking"], "max_score": 18},
                 {"name": "Read Words", "skills": ["Reading"], "max_score": 12},
                 {"name": "Spelling", "skills": ["Spelling", "Writing"], "max_score": 10},
             ]}},
            {"name": "Summer Sports Camp", "start": "2023-07-01", "end": "2023-08-25", "lessons": 16, "days": ["Monday", "Wednesday", "Friday"], "dur": 90,
             "split_mode": "percentage", "subjects": {"Football": 35, "Tennis": 35, "Swimming": 30}, "grade": None,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Ball Control", "skills": ["Dribbling", "Passing"]},
                 {"name": "LO-2: Racket Skills", "skills": ["Forehand", "Backhand"]},
                 {"name": "LO-3: Water Confidence", "skills": ["Freestyle", "Endurance"]},
             ], "max_score": 5}},
            {"name": "Music Fundamentals", "start": "2023-09-01", "end": "2024-06-15", "lessons": 40, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Piano": 50, "Guitar": 30, "Music Theory": 20}, "grade": 92,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Note Reading", "skills": ["Sight Reading"]},
                 {"name": "LO-2: Rhythm Mastery", "skills": ["Rhythm"]},
                 {"name": "LO-3: Performance", "skills": ["Expression", "Technique"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Practical Exam", "skills": ["Technique", "Expression"], "max_score": 30},
                 {"name": "Theory Test", "skills": ["Notation", "Ear Training"], "max_score": 20},
             ]}},
            {"name": "Creative Writing Workshop", "start": "2024-01-10", "end": "2024-06-15", "lessons": 10, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Creative Writing": 60, "English": 40}, "grade": 85,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Story Structure", "skills": ["Writing", "Narrative"]},
                 {"name": "LO-2: Poetry", "skills": ["Reading", "Creativity"]},
                 {"name": "LO-3: Dialogue Writing", "skills": ["Writing", "Speaking"]},
             ], "max_score": 5}},
        ],
    },
    # ═══ PROFILE 2: Oliver Park — Strategy & Leadership ═══
    # Reading/Writing/Spelling appear in RWI-F1(42L) + RWI-F2(40L) + Theatre(10L)
    {
        "name": "Oliver Park", "dob": "2013-07-22", "enrollment": "2023-01-10", "branch": "br_hk_babington",
        "courses": [
            {"name": "RWI - F1", "start": "2023-01-15", "end": "2023-12-10", "lessons": 42, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": 85,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Sounds Recognition", "skills": ["Reading"]},
                 {"name": "LO-2: Word Building", "skills": ["Spelling"]},
                 {"name": "LO-3: Comprehension", "skills": ["Reading", "Comprehension"]},
                 {"name": "LO-4: Expression", "skills": ["Speaking"]},
                 {"name": "LO-5: Handwriting", "skills": ["Writing"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Say The Sounds", "skills": ["Reading", "Speaking"], "max_score": 18},
                 {"name": "Read Words", "skills": ["Reading"], "max_score": 12},
                 {"name": "Spelling Test", "skills": ["Spelling"], "max_score": 10},
             ]}},
            {"name": "RWI - F2", "start": "2024-01-15", "end": "2024-12-10", "lessons": 40, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": 82,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Complex Sounds", "skills": ["Reading", "Spelling"]},
                 {"name": "LO-2: Sentence Writing", "skills": ["Writing", "Grammar"]},
                 {"name": "LO-3: Story Comprehension", "skills": ["Comprehension", "Listening"]},
                 {"name": "LO-4: Fluent Reading", "skills": ["Reading"]},
                 {"name": "LO-5: Vocabulary", "skills": ["Speaking", "Linguistics"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Phonics Assessment", "skills": ["Reading", "Spelling"], "max_score": 20},
                 {"name": "Writing Assessment", "skills": ["Writing", "Grammar"], "max_score": 15},
                 {"name": "Comprehension Test", "skills": ["Comprehension"], "max_score": 15},
                 {"name": "Oral Assessment", "skills": ["Speaking", "Listening"], "max_score": 10},
             ]}},
            {"name": "Chess Academy", "start": "2023-03-01", "end": "2024-02-28", "lessons": 48, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Chess": 70, "Board Games": 30}, "grade": 90,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Opening Repertoire", "skills": ["Opening Theory", "Strategy"]},
                 {"name": "LO-2: Tactical Patterns", "skills": ["Tactics"]},
                 {"name": "LO-3: Endgame Technique", "skills": ["Endgame", "Strategy"]},
             ], "max_score": 5}},
            {"name": "Sports Excellence", "start": "2023-09-01", "end": "2024-06-30", "lessons": 40, "days": ["Wednesday"], "dur": 90,
             "split_mode": "percentage", "subjects": {"Rugby": 40, "Basketball": 30, "Swimming": 30}, "grade": 78,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Team Play", "skills": ["Passing", "Tackling"]},
                 {"name": "LO-2: Shooting Accuracy", "skills": ["Shooting"]},
                 {"name": "LO-3: Swim Technique", "skills": ["Freestyle", "Backstroke"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Fitness Test", "skills": ["Endurance", "Tackling"], "max_score": 25},
                 {"name": "Game Performance", "skills": ["Passing", "Shooting"], "max_score": 20},
             ]}},
            {"name": "Theatre Arts Intensive", "start": "2024-09-01", "end": "2024-11-30", "lessons": 10, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Drama": 40, "Public Speaking": 30, "Creative Writing": 30}, "grade": None,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Character Work", "skills": ["Characterisation", "Expression"]},
                 {"name": "LO-2: Speech & Writing", "skills": ["Speaking", "Writing"]},
             ], "max_score": 5}},
        ],
    },
    # ═══ PROFILE 3: Mia Johnson — STEM & Dance ═══
    # Technique/Expression appear in Ballet(48L) + Art(12L) for big weight difference
    {
        "name": "Mia Johnson", "dob": "2016-11-08", "enrollment": "2024-01-05", "branch": "br_hk_babington",
        "courses": [
            {"name": "English Ladder - S1M1", "start": "2024-01-10", "end": "2024-12-15", "lessons": 42, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": 75,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Reading Accuracy", "skills": ["Reading", "Comprehension"]},
                 {"name": "LO-2: Written Expression", "skills": ["Writing", "Grammar"]},
                 {"name": "LO-3: Listening Skills", "skills": ["Listening"]},
                 {"name": "LO-4: Speaking Fluency", "skills": ["Speaking"]},
             ], "max_score": 5}},
            {"name": "Ballet & Contemporary", "start": "2024-03-01", "end": "2025-02-28", "lessons": 48, "days": ["Tuesday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Ballet": 50, "Contemporary Dance": 50}, "grade": 95,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Technical Form", "skills": ["Technique", "Posture"]},
                 {"name": "LO-2: Artistic Expression", "skills": ["Expression", "Fluidity"]},
                 {"name": "LO-3: Flexibility & Balance", "skills": ["Flexibility", "Balance"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Technique Exam", "skills": ["Technique", "Posture"], "max_score": 30},
                 {"name": "Performance Piece", "skills": ["Expression"], "max_score": 20},
             ]}},
            {"name": "Science Explorers", "start": "2024-09-01", "end": "2025-06-30", "lessons": 40, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Science": 50, "Robotics": 30, "Coding": 20}, "grade": 88,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Lab Skills", "skills": ["Observation", "Experimentation"]},
                 {"name": "LO-2: Programming", "skills": ["Logic", "Syntax"]},
                 {"name": "LO-3: Robot Design", "skills": ["Design", "Mechanics"]},
             ], "max_score": 5}},
            {"name": "Art Studio Crash Course", "start": "2024-06-01", "end": "2024-08-31", "lessons": 12, "days": ["Wednesday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Painting": 35, "Drawing": 35, "Sculpture": 30}, "grade": 91,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Mixed Media", "skills": ["Technique", "Creativity"]},
                 {"name": "LO-2: Drawing Fundamentals", "skills": ["Line Work", "Perspective"]},
                 {"name": "LO-3: Artistic Expression", "skills": ["Expression", "Composition"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Portfolio Review", "skills": ["Composition", "Creativity"], "max_score": 25},
                 {"name": "Final Piece", "skills": ["Technique", "Expression"], "max_score": 25},
             ]}},
        ],
    },
    # ═══ PROFILE 4: James Lee — Academic + Leadership ═══
    # Reading/Writing/Grammar appear in Academic(96L) + RWI(40L) + Coding(12L)
    {
        "name": "James Lee", "dob": "2012-05-20", "enrollment": "2022-01-15", "branch": "br_hk_babington",
        "courses": [
            {"name": "Academic Excellence", "start": "2022-01-20", "end": "2023-12-15", "lessons": 96, "days": ["Monday", "Friday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 30, "Mathematics": 30, "Science": 20, "History": 20}, "grade": 92,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Advanced Reading", "skills": ["Reading", "Comprehension"]},
                 {"name": "LO-2: Mathematical Reasoning", "skills": ["Problem Solving", "Algebra"]},
                 {"name": "LO-3: Scientific Method", "skills": ["Experimentation"]},
                 {"name": "LO-4: Essay Writing", "skills": ["Writing", "Grammar"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "English Exam", "skills": ["Reading", "Writing", "Grammar"], "max_score": 40},
                 {"name": "Maths Exam", "skills": ["Arithmetic", "Algebra"], "max_score": 40},
                 {"name": "Science Practical", "skills": ["Experimentation", "Observation"], "max_score": 20},
             ]}},
            {"name": "RWI - Elementary 1 - Green", "start": "2022-09-01", "end": "2023-06-30", "lessons": 40, "days": ["Wednesday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": 87,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Advanced Phonics", "skills": ["Reading", "Spelling"]},
                 {"name": "LO-2: Complex Sentences", "skills": ["Writing", "Grammar"]},
                 {"name": "LO-3: Reading Aloud", "skills": ["Speaking", "Reading"]},
                 {"name": "LO-4: Comprehension", "skills": ["Comprehension", "Listening"]},
                 {"name": "LO-5: Behaviour", "skills": ["Behaviour"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Read Words", "skills": ["Reading"], "max_score": 20},
                 {"name": "Spelling", "skills": ["Spelling", "Writing"], "max_score": 15},
                 {"name": "Comprehension", "skills": ["Comprehension"], "max_score": 15},
                 {"name": "Grammar", "skills": ["Grammar"], "max_score": 10},
             ]}},
            {"name": "Leadership Programme", "start": "2023-01-15", "end": "2024-06-30", "lessons": 50, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Public Speaking": 30, "Debate": 25, "Team Building": 25, "Community Service": 20}, "grade": 80,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Public Address", "skills": ["Confidence", "Delivery"]},
                 {"name": "LO-2: Debate Skills", "skills": ["Argumentation", "Rebuttal"]},
                 {"name": "LO-3: Team Leadership", "skills": ["Leadership", "Communication"]},
             ], "max_score": 5}},
            {"name": "Coding Bootcamp Sprint", "start": "2024-01-10", "end": "2024-04-15", "lessons": 12, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Coding": 60, "Robotics": 40}, "grade": 95,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Programming Logic", "skills": ["Logic", "Problem Solving"]},
                 {"name": "LO-2: Code Quality", "skills": ["Syntax", "Debugging"]},
                 {"name": "LO-3: Reading Documentation", "skills": ["Reading", "Comprehension"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Coding Challenge", "skills": ["Logic", "Syntax"], "max_score": 30},
                 {"name": "Robot Build", "skills": ["Design", "Mechanics"], "max_score": 20},
             ]}},
            {"name": "Photography & Visual Arts", "start": "2024-06-01", "end": "2025-05-31", "lessons": 38, "days": ["Thursday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Photography": 40, "Drawing": 30, "Digital Art": 30}, "grade": None,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Composition", "skills": ["Composition", "Lighting"]},
                 {"name": "LO-2: Illustration", "skills": ["Line Work", "Shading"]},
                 {"name": "LO-3: Digital Creation", "skills": ["Software Skills", "Creativity"]},
             ], "max_score": 5}},
        ],
    },
    # ═══ PROFILE 5: Emma Wilson — Music & Languages ═══
    # Reading/Writing/Speaking in English(40L) + French(42L) + Short Workshop(8L)
    {
        "name": "Emma Wilson", "dob": "2014-09-12", "enrollment": "2023-09-01", "branch": "br_hk_babington",
        "courses": [
            {"name": "English Ladder - S1M1", "start": "2023-09-05", "end": "2024-06-20", "lessons": 40, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": 80,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Reading Skills", "skills": ["Reading", "Comprehension"]},
                 {"name": "LO-2: Writing Ability", "skills": ["Writing", "Spelling"]},
                 {"name": "LO-3: Communication", "skills": ["Speaking", "Listening"]},
             ], "max_score": 5}},
            {"name": "Piano & Voice", "start": "2023-09-01", "end": "2024-08-31", "lessons": 48, "days": ["Tuesday"], "dur": 45,
             "split_mode": "percentage", "subjects": {"Piano": 50, "Singing": 50}, "grade": 93,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Piano Technique", "skills": ["Technique", "Sight Reading"]},
                 {"name": "LO-2: Vocal Control", "skills": ["Pitch", "Breath Control"]},
                 {"name": "LO-3: Musical Expression", "skills": ["Expression", "Rhythm"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Piano Recital", "skills": ["Technique", "Expression"], "max_score": 25},
                 {"name": "Vocal Performance", "skills": ["Pitch", "Breath Control"], "max_score": 25},
             ]}},
            {"name": "French Beginners", "start": "2024-01-10", "end": "2024-12-15", "lessons": 42, "days": ["Thursday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"French": 100}, "grade": 72,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: French Reading", "skills": ["Reading", "Comprehension"]},
                 {"name": "LO-2: French Grammar", "skills": ["Grammar", "Writing"]},
                 {"name": "LO-3: Oral French", "skills": ["Speaking", "Listening"]},
             ], "max_score": 5}},
            {"name": "Speaking & Reading Sprint", "start": "2024-06-01", "end": "2024-07-31", "lessons": 8, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 50, "Public Speaking": 50}, "grade": 90,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Confident Speaking", "skills": ["Speaking", "Confidence"]},
                 {"name": "LO-2: Critical Reading", "skills": ["Reading", "Comprehension"]},
             ], "max_score": 5}},
        ],
    },
    # ═══ PROFILE 6: Ethan Tanaka — Sports & Strategy ═══
    {
        "name": "Ethan Tanaka", "dob": "2013-02-28", "enrollment": "2022-06-01", "branch": "br_hk_babington",
        "courses": [
            {"name": "RWI - F2", "start": "2022-09-05", "end": "2023-06-20", "lessons": 38, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": 78,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Advanced Sounds", "skills": ["Reading", "Spelling"]},
                 {"name": "LO-2: Story Writing", "skills": ["Writing", "Grammar"]},
                 {"name": "LO-3: Active Listening", "skills": ["Listening", "Comprehension"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Phonics Test", "skills": ["Reading", "Spelling"], "max_score": 20},
                 {"name": "Writing Test", "skills": ["Writing", "Grammar"], "max_score": 15},
             ]}},
            {"name": "Martial Arts Dojo", "start": "2022-06-10", "end": "2023-06-10", "lessons": 50, "days": ["Monday", "Thursday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Karate": 50, "Judo": 50}, "grade": 88,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Kata Performance", "skills": ["Kata", "Discipline"]},
                 {"name": "LO-2: Sparring", "skills": ["Kumite"]},
                 {"name": "LO-3: Groundwork", "skills": ["Groundwork", "Balance"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Belt Grading", "skills": ["Kata", "Kumite", "Discipline"], "max_score": 30},
                 {"name": "Technique Assessment", "skills": ["Groundwork", "Balance"], "max_score": 20},
             ]}},
            {"name": "Football Academy", "start": "2023-09-01", "end": "2024-06-30", "lessons": 40, "days": ["Wednesday"], "dur": 90,
             "split_mode": "percentage", "subjects": {"Football": 100}, "grade": 82,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Ball Control", "skills": ["Dribbling", "Passing"]},
                 {"name": "LO-2: Game Play", "skills": ["Shooting", "Tackling"]},
                 {"name": "LO-3: Discipline", "skills": ["Discipline"]},
             ], "max_score": 5}},
            {"name": "Short Coding Camp", "start": "2024-07-01", "end": "2024-08-15", "lessons": 10, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Coding": 70, "Robotics": 30}, "grade": 91,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Algorithms", "skills": ["Logic", "Problem Solving"]},
                 {"name": "LO-2: Code Crafting", "skills": ["Syntax", "Debugging"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Project Submission", "skills": ["Logic", "Syntax"], "max_score": 30},
                 {"name": "Presentation", "skills": ["Problem Solving"], "max_score": 15},
             ]}},
        ],
    },
    # ═══ PROFILE 7: Sophia Martinez — Dance & Creative ═══
    # Rhythm/Coordination in HipHop(48L) + Swimming(10L) for weight divergence
    {
        "name": "Sophia Martinez", "dob": "2015-06-15", "enrollment": "2024-03-01", "branch": "br_hk_babington",
        "courses": [
            {"name": "RWI - F1", "start": "2024-03-05", "end": "2025-02-28", "lessons": 44, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": None,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Letter Sounds", "skills": ["Reading", "Spelling"]},
                 {"name": "LO-2: Simple Words", "skills": ["Reading", "Comprehension"]},
                 {"name": "LO-3: Writing Letters", "skills": ["Writing"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Sounds Test", "skills": ["Reading", "Speaking"], "max_score": 18},
                 {"name": "Writing Test", "skills": ["Writing", "Spelling"], "max_score": 12},
             ]}},
            {"name": "Hip Hop & Pop Dance", "start": "2024-04-01", "end": "2025-03-31", "lessons": 48, "days": ["Tuesday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Hip Hop": 50, "Pop Dance": 50}, "grade": 90,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Rhythm & Groove", "skills": ["Rhythm", "Coordination"]},
                 {"name": "LO-2: Choreography", "skills": ["Choreography", "Performance"]},
                 {"name": "LO-3: Freestyle", "skills": ["Freestyle", "Isolation"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Solo Performance", "skills": ["Performance", "Rhythm"], "max_score": 25},
                 {"name": "Group Routine", "skills": ["Coordination", "Choreography"], "max_score": 25},
             ]}},
            {"name": "Musical Theatre", "start": "2024-09-01", "end": "2025-06-30", "lessons": 38, "days": ["Sunday"], "dur": 90,
             "split_mode": "percentage", "subjects": {"Musical Theatre": 40, "Singing": 30, "Drama": 30}, "grade": 85,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Triple Threat", "skills": ["Singing", "Acting", "Dance"]},
                 {"name": "LO-2: Stage Performance", "skills": ["Expression", "Performance"]},
             ], "max_score": 5}},
            {"name": "Swimming Crash Course", "start": "2024-06-01", "end": "2024-07-31", "lessons": 10, "days": ["Thursday"], "dur": 45,
             "split_mode": "percentage", "subjects": {"Swimming": 100}, "grade": 75,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Stroke Technique", "skills": ["Freestyle", "Backstroke"]},
                 {"name": "LO-2: Fitness & Coordination", "skills": ["Endurance", "Coordination"]},
             ], "max_score": 5}},
        ],
    },
    # ═══ PROFILE 8: Liam Chen — Academic & Tech ═══
    # Reading/Logic appear in EL3(40L) + STEM(40L) + Chess(42L) + RWI(8L short)
    {
        "name": "Liam Chen", "dob": "2014-12-01", "enrollment": "2023-06-01", "branch": "br_hk_babington",
        "courses": [
            {"name": "English Ladder - S3M1", "start": "2023-09-05", "end": "2024-06-20", "lessons": 40, "days": ["Saturday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": 83,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Advanced Reading", "skills": ["Reading", "Comprehension"]},
                 {"name": "LO-2: Essay Skills", "skills": ["Writing", "Grammar"]},
                 {"name": "LO-3: Discussion", "skills": ["Speaking", "Listening"]},
             ], "max_score": 5}},
            {"name": "STEM Discovery", "start": "2023-09-01", "end": "2024-06-30", "lessons": 40, "days": ["Sunday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Mathematics": 40, "Science": 30, "Coding": 30}, "grade": 90,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Problem Solving", "skills": ["Problem Solving", "Algebra"]},
                 {"name": "LO-2: Lab Work", "skills": ["Experimentation", "Observation"]},
                 {"name": "LO-3: Programming", "skills": ["Logic", "Debugging"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Maths Test", "skills": ["Arithmetic", "Algebra"], "max_score": 30},
                 {"name": "Science Practical", "skills": ["Experimentation"], "max_score": 20},
                 {"name": "Code Review", "skills": ["Logic", "Syntax"], "max_score": 20},
             ]}},
            {"name": "Chess & Strategy", "start": "2024-01-10", "end": "2024-12-15", "lessons": 42, "days": ["Wednesday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Chess": 60, "Board Games": 40}, "grade": 87,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Tactical Mastery", "skills": ["Tactics", "Strategy"]},
                 {"name": "LO-2: Game Analysis", "skills": ["Critical Thinking", "Planning"]},
                 {"name": "LO-3: Logical Thinking", "skills": ["Logic"]},
             ], "max_score": 5}},
            {"name": "Tennis Academy", "start": "2024-06-01", "end": "2025-05-31", "lessons": 44, "days": ["Tuesday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"Tennis": 70, "Running": 30}, "grade": None,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Serve & Volley", "skills": ["Serving", "Footwork"]},
                 {"name": "LO-2: Ground Strokes", "skills": ["Forehand", "Backhand"]},
                 {"name": "LO-3: Fitness", "skills": ["Endurance", "Sprint"]},
             ], "max_score": 5},
             "assessment": {"sections": [
                 {"name": "Match Play", "skills": ["Serving", "Forehand", "Backhand"], "max_score": 30},
                 {"name": "Fitness Test", "skills": ["Endurance", "Sprint"], "max_score": 15},
             ]}},
            {"name": "RWI - F3", "start": "2024-09-01", "end": "2024-10-31", "lessons": 8, "days": ["Friday"], "dur": 60,
             "split_mode": "percentage", "subjects": {"English": 100}, "grade": None,
             "fpr": {"learning_objectives": [
                 {"name": "LO-1: Fluent Reading", "skills": ["Reading"]},
                 {"name": "LO-2: Spelling Patterns", "skills": ["Spelling", "Writing"]},
                 {"name": "LO-3: Comprehension", "skills": ["Comprehension"]},
                 {"name": "LO-4: Speaking Skills", "skills": ["Speaking", "Listening"]},
             ], "max_score": 5}},
        ],
    },
]


# ══════════════════════════════════════════════════════════════════════
# ── BABINGTON CLIENT DATA                                            ──
# ── Source: Babington_Course_Descriptions.xlsx                       ──
# ── Extracted: 27 Feb 2026                                           ──
# ──                                                                  ──
# ── EXCLUDED: "RWI - F4" — 0 LOs, 1 orphaned assessment section.    ──
# ── Likely consolidated into "RWI - F4&5". Confirm with Oliver.      ──
# ──                                                                  ──
# ── UNIFIED SCHEMA (FPR + Assessment — identical structure):         ──
#    record_type     : "fpr_lo" | "assessment_section"                ──
#    program         : "RWI" | "English Ladder"                       ──
#    course          : "<Program> - <Level>"  (unique course key)     ──
#    level           : raw level code e.g. "F1", "S1M1"              ──
#    lo_index        : int — LO position within course (fpr_lo only)  ──
#    section_index   : int — section # (assessment_section only)      ──
#    title           : LO text or assessment section title             ──
#    skill_categories: list — already split on "and" / "&"            ──
#    num_skills      : len(skill_categories) — drives F-02/F-02b split──
#    max_score       : 5.0 for LOs | variable for assessment sections  ──
# ──                                                                  ──
# ── CALCULATION FRAMEWORK (Linxed_Finalized_Calculation_Framework):  ──
# ──                                                                  ──
# ── THE SAME FORMULA SET APPLIES TO BOTH FPR LOs AND ASSESSMENTS:   ──
# ──                                                                  ──
# ── COURSE LEVEL (per record):                                       ──
#    F-01a  xp_per_lo       = base_xp / num_los        (fpr_lo)       ──
#    F-01b  xp_per_section  = base_xp / num_sections   (assessment)   ──
#    F-02a  sub_skill_xp    = xp_per_lo / num_skills    (if multi)     ──
#    F-02b  sub_skill_xp    = xp_per_section / num_skills (if multi)   ──
#    F-03   pct_score       = actual_score / max_score                ──
#    F-04   weighted_score  = pct_score * sub_skill_xp                ──
# ──                                                                  ──
# ── CROSS-COURSE LEVEL (per skill, across ALL records FPR+Assessment)──
#    F-05   avg_skill_score    = MEAN(all pct_scores for skill)       ──
#    F-06   avg_wtd_xp_score   = SUM(weighted) / SUM(xp_weights)     ──
# ──                                                                  ──
# ── KEY INSIGHT: FPR LOs and Assessment Sections are BOTH just       ──
# ── "skill-rows" in the aggregation. They feed the same F-05/F-06.   ──
# ── Only difference: XP anchor is num_los vs num_sections.           ──
# ══════════════════════════════════════════════════════════════════════

# ── BABINGTON_COURSE_META ───────────────────────────────────────────
# 34 courses: RWI (11) + English Ladder (23)
# base_xp set at runtime: sessions * 0.6
# xp_per_lo     = base_xp / num_los      (F-01a) — set at runtime
# xp_per_section= base_xp / num_sections (F-01b) — set at runtime
BABINGTON_COURSE_META = {
    'English Ladder - S10': {
        "program": 'English Ladder',
        "level": 'S10',
        "num_los": 14,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S1M1': {
        "program": 'English Ladder',
        "level": 'S1M1',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S1M2': {
        "program": 'English Ladder',
        "level": 'S1M2',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S1M3': {
        "program": 'English Ladder',
        "level": 'S1M3',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S2M1': {
        "program": 'English Ladder',
        "level": 'S2M1',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S2M2': {
        "program": 'English Ladder',
        "level": 'S2M2',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S2M3': {
        "program": 'English Ladder',
        "level": 'S2M3',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S3M1': {
        "program": 'English Ladder',
        "level": 'S3M1',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S3M2': {
        "program": 'English Ladder',
        "level": 'S3M2',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S3M3': {
        "program": 'English Ladder',
        "level": 'S3M3',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S4': {
        "program": 'English Ladder',
        "level": 'S4',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S5M1': {
        "program": 'English Ladder',
        "level": 'S5M1',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S5M2': {
        "program": 'English Ladder',
        "level": 'S5M2',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S5M3': {
        "program": 'English Ladder',
        "level": 'S5M3',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S6M1': {
        "program": 'English Ladder',
        "level": 'S6M1',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S6M2': {
        "program": 'English Ladder',
        "level": 'S6M2',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S6M3': {
        "program": 'English Ladder',
        "level": 'S6M3',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S7M1': {
        "program": 'English Ladder',
        "level": 'S7M1',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S7M2': {
        "program": 'English Ladder',
        "level": 'S7M2',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S7M3': {
        "program": 'English Ladder',
        "level": 'S7M3',
        "num_los": 15,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S8M1': {
        "program": 'English Ladder',
        "level": 'S8M1',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S8M2': {
        "program": 'English Ladder',
        "level": 'S8M2',
        "num_los": 19,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'English Ladder - S9': {
        "program": 'English Ladder',
        "level": 'S9',
        "num_los": 14,
        "num_sections": 0,
        "has_fpr": True,
        "has_assessment": False,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - Advanced 1 - Yellow': {
        "program": 'RWI',
        "level": 'Advanced 1 - Yellow',
        "num_los": 15,
        "num_sections": 6,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - Advanced 2 - Blue': {
        "program": 'RWI',
        "level": 'Advanced 2 - Blue',
        "num_los": 15,
        "num_sections": 6,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - Elementary 1 - Green': {
        "program": 'RWI',
        "level": 'Elementary 1 - Green',
        "num_los": 14,
        "num_sections": 7,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - Elementary 2 - Purple': {
        "program": 'RWI',
        "level": 'Elementary 2 - Purple',
        "num_los": 14,
        "num_sections": 8,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - F1': {
        "program": 'RWI',
        "level": 'F1',
        "num_los": 9,
        "num_sections": 3,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - F2': {
        "program": 'RWI',
        "level": 'F2',
        "num_los": 10,
        "num_sections": 5,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - F3': {
        "program": 'RWI',
        "level": 'F3',
        "num_los": 12,
        "num_sections": 6,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - F4&5': {
        "program": 'RWI',
        "level": 'F4&5',
        "num_los": 13,
        "num_sections": 6,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - Intermediate 1 - Pink': {
        "program": 'RWI',
        "level": 'Intermediate 1 - Pink',
        "num_los": 15,
        "num_sections": 9,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - Intermediate 2 - Orange': {
        "program": 'RWI',
        "level": 'Intermediate 2 - Orange',
        "num_los": 15,
        "num_sections": 8,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
    'RWI - Upper Advanced 2 - Grey': {
        "program": 'RWI',
        "level": 'Upper Advanced 2 - Grey',
        "num_los": 15,
        "num_sections": 6,
        "has_fpr": True,
        "has_assessment": True,
        "base_xp": None,       # runtime: sessions * 0.6
        "xp_per_lo": None,      # runtime: base_xp / num_los      (F-01a)
        "xp_per_section": None, # runtime: base_xp / num_sections (F-01b)
    },
}

# ── BABINGTON_COURSE_BLUEPRINT ──────────────────────────────────────
# 596 total records: 526 FPR LOs + 70 Assessment Sections
# All records feed F-03 → F-04 → F-05/F-06 uniformly
BABINGTON_COURSE_BLUEPRINT = [

    # ── RWI - F1 (RWI) | LOs:9 Sections:3 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 4, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 5, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 6, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 7, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 8, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': 9, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - F2 (RWI) | LOs:10 Sections:5 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 5, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 6, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 7, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 9, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': 10, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - F3 (RWI) | LOs:12 Sections:6 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 6, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 7, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 10, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 11, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': 12, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - F4&5 (RWI) | LOs:13 Sections:6 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 7, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 11, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 12, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - Elementary 1 - Green (RWI) | LOs:14 Sections:7 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 7, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 11, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 12, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': 14, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - Elementary 2 - Purple (RWI) | LOs:14 Sections:8 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 7, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 11, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 12, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': 14, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - Intermediate 1 - Pink (RWI) | LOs:15 Sections:9 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 7, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 11, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 12, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 14, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': 15, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - Intermediate 2 - Orange (RWI) | LOs:15 Sections:8 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 7, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 11, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 12, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 14, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': 15, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - Advanced 1 - Yellow (RWI) | LOs:15 Sections:6 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 7, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 11, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 12, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 14, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': 15, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - Advanced 2 - Blue (RWI) | LOs:15 Sections:6 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 7, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 11, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 12, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 14, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': 15, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - Upper Advanced 2 - Grey (RWI) | LOs:15 Sections:6 [FPR+Assessment] ──
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 1, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 2, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 3, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 4, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 5, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 6, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 7, 'section_index': None, 'title': 'comprehension and representing language', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 8, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 9, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 10, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 11, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 12, 'section_index': None, 'title': 'ability to communicate, receive and comprehend communication', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 13, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 14, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': 15, 'section_index': None, 'title': 'actions and mannerisms of an individual', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S1M1 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M1', 'level': 'S1M1', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S1M2 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M2', 'level': 'S1M2', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S1M3 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S1M3', 'level': 'S1M3', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S2M1 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M1', 'level': 'S2M1', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S2M2 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M2', 'level': 'S2M2', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S2M3 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S2M3', 'level': 'S2M3', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S3M1 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M1', 'level': 'S3M1', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S3M2 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M2', 'level': 'S3M2', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S3M3 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S3M3', 'level': 'S3M3', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S4 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 1, 'section_index': None, 'title': 'Recognize individual sounds', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 2, 'section_index': None, 'title': 'Read words using phonics', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 3, 'section_index': None, 'title': 'Read sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 4, 'section_index': None, 'title': 'Read storybooks', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 5, 'section_index': None, 'title': 'Pronounce sounds', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 6, 'section_index': None, 'title': 'Pronounce words', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 7, 'section_index': None, 'title': 'Speak in sentences', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 8, 'section_index': None, 'title': 'Answer comprehension questions (verbally)', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 9, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 10, 'section_index': None, 'title': 'Answer comprehension questions (in writing)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 11, 'section_index': None, 'title': 'Understand and answer grammar questions', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 12, 'section_index': None, 'title': 'Use power words in sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S4', 'level': 'S4', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S5M1 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 17, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M1', 'level': 'S5M1', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S5M2 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 17, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M2', 'level': 'S5M2', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S5M3 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 17, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S5M3', 'level': 'S5M3', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S6M1 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M1', 'level': 'S6M1', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S6M2 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 17, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M2', 'level': 'S6M2', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S6M3 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 17, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S6M3', 'level': 'S6M3', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S7M1 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)\n', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 17, 'section_index': None, 'title': 'Follow instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M1', 'level': 'S7M1', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S7M2 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)\n', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 17, 'section_index': None, 'title': 'Follow instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M2', 'level': 'S7M2', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S7M3 (English Ladder) | LOs:15 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 1, 'section_index': None, 'title': 'Recognize sight words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 2, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 3, 'section_index': None, 'title': 'Recognize individual words', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 4, 'section_index': None, 'title': 'Match vocabulary words to pictures', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 5, 'section_index': None, 'title': 'Speak in sentences frequently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 6, 'section_index': None, 'title': 'Express herself/himself fluently', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 7, 'section_index': None, 'title': 'Use intonation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 8, 'section_index': None, 'title': 'Understand and respond to teachers’ questions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 9, 'section_index': None, 'title': 'Recognize graphemes representing the sound', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 10, 'section_index': None, 'title': 'Write the graphemes independently in written form', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 11, 'section_index': None, 'title': 'Read decodable texts', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 12, 'section_index': None, 'title': 'Spell words using the phonics skill', 'skill_categories': ['Phonics', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 13, 'section_index': None, 'title': 'Follows instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 14, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S7M3', 'level': 'S7M3', 'lo_index': 15, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S8M1 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)\n', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 17, 'section_index': None, 'title': 'Follow instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M1', 'level': 'S8M1', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S8M2 (English Ladder) | LOs:19 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 1, 'section_index': None, 'title': 'Read fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 2, 'section_index': None, 'title': 'Read with rhythm and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 3, 'section_index': None, 'title': 'Decode unfamiliar words (blending)', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 4, 'section_index': None, 'title': 'Write meaningful sentences', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 5, 'section_index': None, 'title': 'Encode unfamiliar words (blending)', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 6, 'section_index': None, 'title': 'Use power words', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 7, 'section_index': None, 'title': 'Presentation of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 8, 'section_index': None, 'title': 'Write grammatically correct sentences', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 9, 'section_index': None, 'title': 'Grasp the grammar concepts', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 10, 'section_index': None, 'title': 'Punctuation', 'skill_categories': ['Grammar'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 11, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 12, 'section_index': None, 'title': 'Able to understand the meaning out of the text\n(e.g. cause and effect)\n', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 13, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Comprehension'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 14, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 15, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 16, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Oral'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 17, 'section_index': None, 'title': 'Follow instructions', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 18, 'section_index': None, 'title': 'Participate in class', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S8M2', 'level': 'S8M2', 'lo_index': 19, 'section_index': None, 'title': 'Cooperate with teacher and students', 'skill_categories': ['Behaviour'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S9 (English Ladder) | LOs:14 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 1, 'section_index': None, 'title': 'Read stories fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 2, 'section_index': None, 'title': 'Read with expression and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 3, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 4, 'section_index': None, 'title': 'Able to understand the text', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 5, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 6, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 7, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 8, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 9, 'section_index': None, 'title': 'Able to understand and join in with discussions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 10, 'section_index': None, 'title': 'Write accurate comprehension responses', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 11, 'section_index': None, 'title': 'Understand and answer grammar questions', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 12, 'section_index': None, 'title': 'Plan written pieces', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 13, 'section_index': None, 'title': 'Use power words in written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S9', 'level': 'S9', 'lo_index': 14, 'section_index': None, 'title': 'Quality of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},

    # ── English Ladder - S10 (English Ladder) | LOs:14 Sections:0 [FPR-only] ──
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 1, 'section_index': None, 'title': 'Read stories fluently', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 2, 'section_index': None, 'title': 'Read with expression and intonation', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 3, 'section_index': None, 'title': 'Able to locate answers in the text', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 4, 'section_index': None, 'title': 'Able to understand the text', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 5, 'section_index': None, 'title': 'Able to relate personal experience to the text', 'skill_categories': ['Reading'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 6, 'section_index': None, 'title': 'Speak fluently and meaningfully', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 7, 'section_index': None, 'title': 'Answer questions in a grammatically correct way', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 8, 'section_index': None, 'title': 'Pronunciation', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 9, 'section_index': None, 'title': 'Able to understand and join in with discussions', 'skill_categories': ['Speaking', 'Listening'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 10, 'section_index': None, 'title': 'Write accurate comprehension responses', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 11, 'section_index': None, 'title': 'Understand and answer grammar questions', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 12, 'section_index': None, 'title': 'Plan written pieces', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 13, 'section_index': None, 'title': 'Use power words in written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},
    {'record_type': 'fpr_lo', 'program': 'English Ladder', 'course': 'English Ladder - S10', 'level': 'S10', 'lo_index': 14, 'section_index': None, 'title': 'Quality of written work', 'skill_categories': ['Writing'], 'num_skills': 1, 'max_score': 5.0},

    # ── RWI - F1 (RWI) | LOs:9 Sections:3 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': None, 'section_index': 1, 'title': 'Say The Sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 18.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': None, 'section_index': 2, 'title': 'Part 2: Oral Blending – Say the sounds and student says the word', 'skill_categories': ['Listening', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F1', 'level': 'F1', 'lo_index': None, 'section_index': 3, 'title': 'Part 3: Fred Talk words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},

    # ── RWI - F2 (RWI) | LOs:10 Sections:5 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': None, 'section_index': 1, 'title': 'Say The Sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 31.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': None, 'section_index': 2, 'title': 'Write The Sounds', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 3.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': None, 'section_index': 3, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': None, 'section_index': 4, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F2', 'level': 'F2', 'lo_index': None, 'section_index': 5, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},

    # ── RWI - F3 (RWI) | LOs:12 Sections:6 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 31.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': None, 'section_index': 2, 'title': 'Write the sounds', 'skill_categories': ['Listening', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': None, 'section_index': 3, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': None, 'section_index': 4, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': None, 'section_index': 5, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F3', 'level': 'F3', 'lo_index': None, 'section_index': 6, 'title': 'Read the Sentence', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},

    # ── RWI - F4&5 (RWI) | LOs:13 Sections:6 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': None, 'section_index': 2, 'title': 'Write the sounds', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': None, 'section_index': 3, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': None, 'section_index': 4, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': None, 'section_index': 5, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': None, 'section_index': 6, 'title': 'Read the Sentence', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - F4&5', 'level': 'F4&5', 'lo_index': None, 'section_index': 6, 'title': 'Hold a Sentence', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 11.0},

    # ── RWI - Elementary 1 - Green (RWI) | LOs:14 Sections:7 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 43.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': None, 'section_index': 2, 'title': 'Write the sounds', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': None, 'section_index': 3, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': None, 'section_index': 4, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': None, 'section_index': 5, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': None, 'section_index': 6, 'title': 'Hold a Sentence', 'skill_categories': ['Listening', 'Speaking', 'Writing'], 'num_skills': 3, 'max_score': 15.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 1 - Green', 'level': 'Elementary 1 - Green', 'lo_index': None, 'section_index': 7, 'title': 'Read a passage', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 22.0},

    # ── RWI - Elementary 2 - Purple (RWI) | LOs:14 Sections:8 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 23.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': 2, 'title': 'Write the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': 3, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': 4, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': 5, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': 6, 'title': 'Hold a Sentence', 'skill_categories': ['Listening', 'Speaking', 'Writing'], 'num_skills': 3, 'max_score': 16.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': 7, 'title': 'Read a passage', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 26.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Elementary 2 - Purple', 'level': 'Elementary 2 - Purple', 'lo_index': None, 'section_index': None, 'title': 'Error Checking', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 3.0},

    # ── RWI - Intermediate 1 - Pink (RWI) | LOs:15 Sections:9 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 12.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 2, 'title': 'Write the sounds', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 3, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 4, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 5, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 6, 'title': 'Hold a Sentence', 'skill_categories': ['Listening', 'Speaking', 'Writing'], 'num_skills': 3, 'max_score': 15.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 7, 'title': 'Read a passage', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 27.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 8, 'title': 'Answer the question', 'skill_categories': ['Reading', 'Comprehension', 'Writing'], 'num_skills': 3, 'max_score': 3.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 1 - Pink', 'level': 'Intermediate 1 - Pink', 'lo_index': None, 'section_index': 9, 'title': 'Error Checking', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 3.0},

    # ── RWI - Intermediate 2 - Orange (RWI) | LOs:15 Sections:8 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 20.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 2, 'title': 'Write the sounds', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 3, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 4, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 5, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 6, 'title': 'Read a passage', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 41.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 7, 'title': 'Answer the question', 'skill_categories': ['Reading', 'Comprehension', 'Writing'], 'num_skills': 3, 'max_score': 3.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Intermediate 2 - Orange', 'level': 'Intermediate 2 - Orange', 'lo_index': None, 'section_index': 8, 'title': 'Error Checking', 'skill_categories': ['Reading', 'Writing'], 'num_skills': 2, 'max_score': 4.0},

    # ── RWI - Advanced 1 - Yellow (RWI) | LOs:15 Sections:6 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 20.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': None, 'section_index': 2, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': None, 'section_index': 3, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': None, 'section_index': 4, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': None, 'section_index': 5, 'title': 'Read a passage', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 26.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 1 - Yellow', 'level': 'Advanced 1 - Yellow', 'lo_index': None, 'section_index': 6, 'title': 'Writing', 'skill_categories': ['Reading', 'Comprehension', 'Writing'], 'num_skills': 3, 'max_score': 20.0},

    # ── RWI - Advanced 2 - Blue (RWI) | LOs:15 Sections:6 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 20.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': None, 'section_index': 2, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': None, 'section_index': 3, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': None, 'section_index': 4, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': None, 'section_index': 5, 'title': 'Read a passage', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 51.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Advanced 2 - Blue', 'level': 'Advanced 2 - Blue', 'lo_index': None, 'section_index': 6, 'title': 'Writing', 'skill_categories': ['Reading', 'Comprehension', 'Writing'], 'num_skills': 3, 'max_score': 20.0},

    # ── RWI - Upper Advanced 2 - Grey (RWI) | LOs:15 Sections:6 [FPR+Assessment] ──
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': None, 'section_index': 1, 'title': 'Say the sounds', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 20.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': None, 'section_index': 2, 'title': 'Green Words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': None, 'section_index': 3, 'title': 'Nonsense words – Say the sounds and say the word', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': None, 'section_index': 4, 'title': 'Spell with Fred Fingers – Green Words', 'skill_categories': ['Listening', 'Writing'], 'num_skills': 2, 'max_score': 5.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': None, 'section_index': 5, 'title': 'Read a passage', 'skill_categories': ['Reading', 'Speaking'], 'num_skills': 2, 'max_score': 58.0},
    {'record_type': 'assessment_section', 'program': 'RWI', 'course': 'RWI - Upper Advanced 2 - Grey', 'level': 'Upper Advanced 2 - Grey', 'lo_index': None, 'section_index': 6, 'title': 'Writing', 'skill_categories': ['Reading', 'Comprehension', 'Writing'], 'num_skills': 3, 'max_score': 20.0},
]

# ── BABINGTON_COURSES_BY_PROGRAM ────────────────────────────────────
BABINGTON_COURSES_BY_PROGRAM = {
    'English Ladder': ['English Ladder - S10', 'English Ladder - S1M1', 'English Ladder - S1M2', 'English Ladder - S1M3', 'English Ladder - S2M1', 'English Ladder - S2M2', 'English Ladder - S2M3', 'English Ladder - S3M1', 'English Ladder - S3M2', 'English Ladder - S3M3', 'English Ladder - S4', 'English Ladder - S5M1', 'English Ladder - S5M2', 'English Ladder - S5M3', 'English Ladder - S6M1', 'English Ladder - S6M2', 'English Ladder - S6M3', 'English Ladder - S7M1', 'English Ladder - S7M2', 'English Ladder - S7M3', 'English Ladder - S8M1', 'English Ladder - S8M2', 'English Ladder - S9'],
    'RWI': ['RWI - Advanced 1 - Yellow', 'RWI - Advanced 2 - Blue', 'RWI - Elementary 1 - Green', 'RWI - Elementary 2 - Purple', 'RWI - F1', 'RWI - F2', 'RWI - F3', 'RWI - F4&5', 'RWI - Intermediate 1 - Pink', 'RWI - Intermediate 2 - Orange', 'RWI - Upper Advanced 2 - Grey'],
}
