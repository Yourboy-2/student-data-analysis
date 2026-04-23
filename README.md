# Student Performance Data Analysis 📊

A Python data analysis project that examines student performance data across multiple courses. Generates insights on grade distribution, course comparisons, top/bottom performers, and the relationship between attendance and marks.

## Features

- **Dataset Overview** — Total records, courses covered, gender breakdown
- **Marks Statistics** — Mean, median, standard deviation, highest/lowest marks
- **Grade Distribution** — Counts and percentages across all grade categories with a text bar chart
- **Course Comparison** — Average, highest, and lowest marks per course with visual bars
- **Top & Bottom Performers** — Ranked lists of highest and lowest scoring students
- **Attendance Insight** — Compares average marks between high and low attendance groups
- **Summary Insights** — Key findings written in plain language
- **Auto Dataset Generation** — If no CSV file is provided, sample data is generated automatically

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| csv module | Data loading and parsing |
| statistics module | Mean, median, standard deviation |
| collections (defaultdict) | Grouping and counting |

## How to Run

```bash
python data_analysis.py
```

No external libraries required (no pandas or numpy needed — built on the Python standard library).

## Bring Your Own Data

Replace `student_data.csv` with your own CSV file. Required columns:

```
student_id, name, age, course, gender, marks, attendance
```

The script will auto-generate a 20-student sample dataset if no file is found.

## Project Structure

```
data_analysis/
│
├── data_analysis.py     # Main analysis script
├── student_data.csv     # Auto-generated sample dataset
└── README.md
```

## Sample Output

```
=======================================================
  STUDENT PERFORMANCE DATA ANALYSIS
  Author: Awenkosi Moyo
=======================================================

=======================================================
  2. MARKS STATISTICS
=======================================================
  Mean (Average)  : 65.40%
  Median          : 65.00%
  Std Deviation   : 18.23%
  Highest Mark    : 94.50%
  Lowest Mark     : 33.00%
  Range           : 61.50%

=======================================================
  3. GRADE DISTRIBUTION
=======================================================
  Grade          Count    Percentage
  -------------------------------------------------------
  Distinction    5        25.0%
  Merit          6        30.0%
  Pass           3        15.0%
  Fail           6        30.0%
```

## Key Concepts Demonstrated

- CSV data loading and parsing with error handling
- Statistical analysis using Python's `statistics` module
- Data grouping and aggregation with `defaultdict`
- Text-based data visualisation (bar charts)
- Clean modular function design
- Generating and writing structured datasets

## Author

**Awenkosi Moyo** — Software Developer | Python | Data Analysis | Backend Development
