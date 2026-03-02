"""
Linxed XP System — Premium Theme CSS
Dark gradient with glassmorphism, inspired by reference_theme.png
"""


def get_premium_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ─── ROOT VARIABLES ─── */
:root {
    --bg-primary: #0a0e1a;
    --bg-secondary: #0f1629;
    --bg-card: rgba(15, 22, 41, 0.7);
    --bg-glass: rgba(20, 30, 55, 0.55);
    --border-glass: rgba(100, 160, 255, 0.12);
    --border-highlight: rgba(100, 180, 255, 0.25);
    --text-primary: #e8edf5;
    --text-secondary: #8b9cc0;
    --text-muted: #5a6a8a;
    --accent-blue: #4ea8ff;
    --accent-green: #34d399;
    --accent-orange: #fb923c;
    --accent-red: #f87171;
    --accent-purple: #a78bfa;
    --accent-cyan: #22d3ee;
    --accent-gold: #fbbf24;
    --glow-blue: 0 0 20px rgba(78, 168, 255, 0.15);
    --font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}

/* ─── GLOBAL OVERRIDES ─── */
.stApp {
    background: linear-gradient(145deg, #060a14 0%, #0a0e1a 30%, #0d1225 60%, #0a0f1e 100%) !important;
    font-family: var(--font-main) !important;
    color: var(--text-primary) !important;
}

.stApp > header { background: transparent !important; }

/* Hide default streamlit elements */
#MainMenu, footer, .stDeployButton { display: none !important; }

/* ─── SIDEBAR ─── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080c18 0%, #0b1020 50%, #0d1228 100%) !important;
    border-right: 1px solid var(--border-glass) !important;
}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown span,
section[data-testid="stSidebar"] label {
    color: var(--text-secondary) !important;
    font-family: var(--font-main) !important;
}

/* ─── SIDEBAR BUTTONS ─── */
section[data-testid="stSidebar"] .stButton > button {
    width: 100% !important;
    background: transparent !important;
    color: var(--text-secondary) !important;
    border: none !important;
    border-left: 3px solid transparent !important;
    border-radius: 0 8px 8px 0 !important;
    padding: 12px 16px !important;
    font-family: var(--font-main) !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    text-align: left !important;
    transition: all 0.25s ease !important;
    margin: 2px 0 !important;
    letter-spacing: 0.02em !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(78, 168, 255, 0.08) !important;
    color: var(--accent-blue) !important;
    border-left: 3px solid var(--accent-blue) !important;
}

/* Active sidebar button style */
section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: rgba(78, 168, 255, 0.12) !important;
    color: var(--accent-blue) !important;
    border-left: 3px solid var(--accent-blue) !important;
    font-weight: 600 !important;
}

/* ─── GLASS CARDS ─── */
.glass-card {
    background: var(--bg-glass) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 14px !important;
    padding: 24px !important;
    margin-bottom: 16px !important;
    box-shadow: var(--glow-blue) !important;
}

.glass-card-sm {
    background: var(--bg-glass) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 12px !important;
    padding: 16px !important;
    margin-bottom: 12px !important;
}

/* ─── METRIC CARDS ─── */
.metric-card {
    background: linear-gradient(135deg, rgba(15, 22, 41, 0.8), rgba(20, 30, 55, 0.6)) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 14px !important;
    padding: 20px 24px !important;
    text-align: center !important;
}

.metric-value {
    font-size: 28px !important;
    font-weight: 700 !important;
    color: var(--accent-blue) !important;
    font-family: var(--font-main) !important;
    line-height: 1.2 !important;
}

.metric-label {
    font-size: 12px !important;
    font-weight: 500 !important;
    color: var(--text-muted) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    margin-top: 6px !important;
}

.metric-green .metric-value { color: var(--accent-green) !important; }
.metric-orange .metric-value { color: var(--accent-orange) !important; }
.metric-purple .metric-value { color: var(--accent-purple) !important; }
.metric-cyan .metric-value { color: var(--accent-cyan) !important; }
.metric-gold .metric-value { color: var(--accent-gold) !important; }
.metric-red .metric-value { color: var(--accent-red) !important; }

/* ─── BADGES & TAGS ─── */
.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.04em;
}
.badge-blue { background: rgba(78, 168, 255, 0.15); color: var(--accent-blue); border: 1px solid rgba(78, 168, 255, 0.3); }
.badge-green { background: rgba(52, 211, 153, 0.15); color: var(--accent-green); border: 1px solid rgba(52, 211, 153, 0.3); }
.badge-orange { background: rgba(251, 146, 60, 0.15); color: var(--accent-orange); border: 1px solid rgba(251, 146, 60, 0.3); }
.badge-purple { background: rgba(167, 139, 250, 0.15); color: var(--accent-purple); border: 1px solid rgba(167, 139, 250, 0.3); }
.badge-gold { background: rgba(251, 191, 36, 0.15); color: var(--accent-gold); border: 1px solid rgba(251, 191, 36, 0.3); }
.badge-red { background: rgba(248, 113, 113, 0.15); color: var(--accent-red); border: 1px solid rgba(248, 113, 113, 0.3); }

/* ─── STATUS INDICATOR ─── */
.status-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 8px;
}
.status-active { background: var(--accent-green); box-shadow: 0 0 8px rgba(52, 211, 153, 0.5); }
.status-inactive { background: var(--accent-orange); }
.status-pending { background: var(--text-muted); }

/* ─── PROGRESS BAR ─── */
.progress-container {
    background: rgba(15, 22, 41, 0.6);
    border-radius: 10px;
    height: 10px;
    overflow: hidden;
    border: 1px solid rgba(100, 160, 255, 0.08);
}
.progress-fill {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, var(--accent-blue), var(--accent-cyan));
    transition: width 0.6s ease;
}
.progress-fill-green { background: linear-gradient(90deg, #059669, var(--accent-green)) !important; }
.progress-fill-gold { background: linear-gradient(90deg, #d97706, var(--accent-gold)) !important; }
.progress-fill-purple { background: linear-gradient(90deg, #7c3aed, var(--accent-purple)) !important; }

/* ─── HEADINGS ─── */
h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
    font-weight: 700 !important;
}

.page-title {
    font-size: 32px !important;
    font-weight: 800 !important;
    color: var(--text-primary) !important;
    margin-bottom: 8px !important;
    letter-spacing: -0.02em !important;
}

.page-subtitle {
    font-size: 14px !important;
    color: var(--text-muted) !important;
    font-weight: 400 !important;
    margin-bottom: 24px !important;
}

.section-title {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    margin-bottom: 16px !important;
    padding-bottom: 8px !important;
    border-bottom: 1px solid var(--border-glass) !important;
}

/* ─── FORM INPUTS ─── */
.stTextInput > div > div,
.stNumberInput > div > div > input,
.stDateInput > div > div > input,
.stSelectbox > div > div {
    background: rgba(15, 22, 41, 0.8) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
    font-size: 14px !important;
}

.stTextInput > label,
.stNumberInput > label,
.stDateInput > label,
.stSelectbox > label,
.stMultiSelect > label,
.stRadio > label,
.stCheckbox > label,
.stSlider > label {
    color: var(--text-secondary) !important;
    font-family: var(--font-main) !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

/* ─── BUTTONS (Main Content) ─── */
.stButton > button {
    font-family: var(--font-main) !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    transition: all 0.25s ease !important;
    font-size: 14px !important;
    letter-spacing: 0.02em !important;
}

div[data-testid="stMainBlockContainer"] .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #2563eb, #3b82f6) !important;
    color: white !important;
    border: none !important;
    padding: 10px 24px !important;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3) !important;
}

div[data-testid="stMainBlockContainer"] .stButton > button[kind="primary"]:hover {
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.45) !important;
    transform: translateY(-1px) !important;
}

div[data-testid="stMainBlockContainer"] .stButton > button[kind="secondary"] {
    background: transparent !important;
    color: var(--accent-blue) !important;
    border: 1px solid var(--border-highlight) !important;
}

/* Delete button */
.delete-btn button {
    background: rgba(248, 113, 113, 0.1) !important;
    color: var(--accent-red) !important;
    border: 1px solid rgba(248, 113, 113, 0.3) !important;
}

/* ─── TABLES ─── */
.stDataFrame {
    border-radius: 12px !important;
    overflow: hidden !important;
}

.stDataFrame [data-testid="stDataFrameResizable"] {
    border: 1px solid var(--border-glass) !important;
    border-radius: 12px !important;
}

/* ─── TABS ─── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0 !important;
    background: rgba(15, 22, 41, 0.5) !important;
    border-radius: 12px !important;
    padding: 4px !important;
    border: 1px solid var(--border-glass) !important;
}

.stTabs [data-baseweb="tab"] {
    color: var(--text-muted) !important;
    font-family: var(--font-main) !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
}

.stTabs [aria-selected="true"] {
    background: rgba(78, 168, 255, 0.12) !important;
    color: var(--accent-blue) !important;
}

/* ─── EXPANDER ─── */
.streamlit-expanderHeader {
    background: var(--bg-glass) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
    font-weight: 600 !important;
}

/* ─── DIVIDER ─── */
hr {
    border-color: var(--border-glass) !important;
    margin: 24px 0 !important;
}

/* ─── SCROLLBAR ─── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(100, 160, 255, 0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(100, 160, 255, 0.35); }

/* ─── PLOTLY OVERRIDES ─── */
.js-plotly-plot .plotly .main-svg { background: transparent !important; }

/* ─── SELECTBOX DROPDOWN ─── */
[data-baseweb="select"] > div {
    background: rgba(15, 22, 41, 0.8) !important;
    border-color: var(--border-glass) !important;
    border-radius: 10px !important;
}

/* ─── MULTISELECT ─── */
.stMultiSelect > div > div {
    background: rgba(15, 22, 41, 0.8) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 10px !important;
}

/* ─── TOAST / ALERT ─── */
.stAlert {
    background: var(--bg-glass) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
}

/* ─── BRANDED HEADER ─── */
.brand-header {
    padding: 20px 0 16px 0;
    margin-bottom: 20px;
    border-bottom: 1px solid var(--border-glass);
}

.brand-name {
    font-size: 22px;
    font-weight: 800;
    background: linear-gradient(135deg, #4ea8ff, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.02em;
}

.brand-subtitle {
    font-size: 10px;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-top: 2px;
}

/* ─── SYSTEM STATUS ─── */
.system-status {
    background: var(--bg-glass);
    border: 1px solid var(--border-glass);
    border-radius: 12px;
    padding: 16px;
    margin-top: 16px;
}

.system-status-title {
    font-size: 10px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 12px;
}

.system-stat {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
    font-size: 12px;
}

.system-stat-label { color: var(--text-muted); }
.system-stat-value { color: var(--accent-green); font-weight: 600; }

/* ─── COMING SOON ─── */
.coming-soon {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 80px 40px;
    text-align: center;
}

.coming-soon-icon {
    font-size: 48px;
    margin-bottom: 16px;
    opacity: 0.3;
}

.coming-soon-text {
    font-size: 20px;
    font-weight: 600;
    color: var(--text-muted);
}

.coming-soon-sub {
    font-size: 13px;
    color: var(--text-muted);
    opacity: 0.6;
    margin-top: 8px;
}

/* ─── FORMULA DISPLAY ─── */
.formula-block {
    background: rgba(10, 14, 26, 0.8);
    border: 1px solid var(--border-glass);
    border-left: 3px solid var(--accent-blue);
    border-radius: 0 10px 10px 0;
    padding: 16px 20px;
    margin: 12px 0;
    font-family: var(--font-mono);
    font-size: 13px;
    color: var(--accent-cyan);
    line-height: 1.6;
}

.formula-title {
    color: var(--text-primary);
    font-family: var(--font-main);
    font-weight: 700;
    font-size: 15px;
    margin-bottom: 4px;
}

.formula-desc {
    color: var(--text-secondary);
    font-family: var(--font-main);
    font-size: 12px;
    font-weight: 400;
    margin-bottom: 8px;
}

/* ─── NUMBER INPUT WIDTH FIX ─── */
.stNumberInput { max-width: 200px !important; }

/* ─── GLOSSARY ─── */
.glossary-term {
    color: var(--accent-blue);
    font-weight: 600;
    font-size: 14px;
}

.glossary-def {
    color: var(--text-secondary);
    font-size: 13px;
    padding-left: 16px;
    border-left: 2px solid var(--border-glass);
    margin: 4px 0 16px 0;
}
</style>
"""


def metric_card(value, label, color_class=""):
    """Generate HTML for a metric card."""
    return f"""
    <div class="metric-card {color_class}">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """


def progress_bar(pct, fill_class=""):
    """Generate HTML progress bar."""
    return f"""
    <div class="progress-container">
        <div class="progress-fill {fill_class}" style="width: {min(100, max(0, pct))}%"></div>
    </div>
    """


def badge_html(text, color="blue"):
    return f'<span class="badge badge-{color}">{text}</span>'


def status_dot(status="active"):
    return f'<span class="status-dot status-{status}"></span>'
