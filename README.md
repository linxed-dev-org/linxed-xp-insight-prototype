# Linxed XP Framework v4.0

This is a Streamlit-based framework for calculating and visualizing XP (Experience Points) and Skill progression for students in the Linxed ecosystem.

## Features

- **Student Profile Builder**: Create and manage student profiles with course schedules.
- **Data Dashboard**: Overview of courses, subjects, and attendance.
- **Calculation Pipeline**: Transparent view of the 11-level XP hierarchy and decay mechanics.
- **Skills Calculation**: Detailed breakdown of Final Progress Reports (FPR) and Assessment scores.
- **XP Overview**: Level status, badges, and category-wise performance.
- **Insights & Charts**: Visual data storytelling about student growth and activity.

## Project Structure

- `app.py`: Main Streamlit application entry point.
- `xp_engine.py`: Core logic for XP calculations and hierarchy.
- `skills_engine.py`: Logic for skill assessment and aggregation.
- `database.py`: Persistence layer (SQLite).
- `config.py`: Configuration and constants.
- `mock_generator.py`: Utilities for generating sample data.
- `theme.py`: UI/UX styling and custom components.

## Setup and Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/linxed-dev-org/linxed-xp-insight-prototype.git
    cd linxed-xp-insight-prototype
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Usage

- Upon launch, the app will automatically generate dummy student profiles if the database is empty.
- Use the sidebar to navigate between different views (Dashboard, Calculations, Overview, etc.).
- You can override decay rates or create new student profiles directly from the UI.

---
*Created by Linxed Development Team*
