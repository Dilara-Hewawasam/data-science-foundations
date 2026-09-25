# data-science-foundations
My one month foundation project for learning first steps of data science
# Data Science & Statistical Foundations

This repository tracks my hands-on technical preparation and micro-projects in quantitative data science, statistics, and software development.

## Week 1 Micro-Project: Academic & Research Performance EDA

### Project Overview
Analyzed a dataset evaluating student hours, theoretical proficiency, and coding capability across academic departments (Computer Science, Statistics, Mathematics). 

### Key Technical Achievements
- **Environment & Control:** Configured virtual environment (`venv`) and managed Git commit pipeline.
- **Data Cleaning & Imputation:** Detected null values and performed mean/median imputation on missing continuous metrics.
- **Feature Engineering:** Built a weighted performance metric (`Composite_Score`) and boolean filter flags (`High_Capacity`).
- **Aggregation:** Grouped metrics by academic department to evaluate relative performance across disciplines.

### Key Insights
- Computer Science and Statistics majors demonstrated higher average composite scores paired with higher weekly commitment hours.
- Automated pipeline generates exported summary outputs (`week1_cleaned_data.csv`) for reproducible workflows.

### Structure
- `day1_script.py` - Git & Python workspace validation.
- `day2_pandas_intro.py` - Pandas DataFrame structures and summary statistics.
- `day3_eda_basics.py` - Boolean indexing, filtering, and imputation.
- `week1_capstone.py` - Complete Week 1 Capstone pipeline.