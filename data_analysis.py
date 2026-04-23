"""
Data Analysis: Student Performance Report
Author: Awenkosi Moyo
Description: Analyses a student dataset to uncover performance trends, grade
             distributions, course comparisons, and key insights.
             Written as a standalone Python script (mirrors Jupyter Notebook logic).
Tech: Python, CSV, statistics module, string formatting
"""

import csv
import os
import statistics
from collections import defaultdict


# ─── Load Data ────────────────────────────────────────────────────────────────
def load_data(filepath):
    """Load student data from a CSV file and return as a list of dicts."""
    students = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["marks"] = float(row["marks"])
                row["age"] = int(row["age"])
                students.append(row)
            except ValueError:
                continue  # Skip malformed rows
    return students


def generate_sample_data(filepath):
    """Generate a sample dataset if no file is provided."""
    sample = [
        ["student_id", "name", "age", "course", "gender", "marks", "attendance"],
        ["STU001", "Awenkosi Moyo",     22, "Information Technology", "Male",   82.5, 91],
        ["STU002", "Jane Smith",        21, "Computer Science",       "Female", 67.0, 85],
        ["STU003", "Sipho Dlamini",     23, "Software Development",   "Male",   55.5, 78],
        ["STU004", "Priya Naidoo",      20, "Information Technology", "Female", 91.0, 96],
        ["STU005", "Liam Johnson",      22, "Computer Science",       "Male",   44.0, 60],
        ["STU006", "Nomsa Khumalo",     24, "Software Development",   "Female", 73.5, 88],
        ["STU007", "Ethan Williams",    21, "Information Technology", "Male",   38.0, 55],
        ["STU008", "Fatima Osman",      22, "Computer Science",       "Female", 88.0, 94],
        ["STU009", "Thandeka Zulu",     23, "Software Development",   "Female", 61.0, 82],
        ["STU010", "Carlos Ferreira",   20, "Information Technology", "Male",   76.0, 90],
        ["STU011", "Lerato Molefe",     21, "Computer Science",       "Female", 52.0, 70],
        ["STU012", "James Okafor",      25, "Software Development",   "Male",   47.0, 65],
        ["STU013", "Sara Petersen",     22, "Information Technology", "Female", 94.5, 98],
        ["STU014", "Bongani Ndlovu",    21, "Computer Science",       "Male",   69.0, 80],
        ["STU015", "Ayesha Patel",      23, "Software Development",   "Female", 85.0, 93],
        ["STU016", "Michael Botha",     24, "Information Technology", "Male",   41.0, 58],
        ["STU017", "Zanele Sithole",    20, "Computer Science",       "Female", 79.0, 87],
        ["STU018", "David Mahlangu",    22, "Software Development",   "Male",   63.0, 75],
        ["STU019", "Ingrid van Wyk",    21, "Information Technology", "Female", 57.0, 72],
        ["STU020", "Kabelo Mokoena",    23, "Computer Science",       "Male",   33.0, 50],
    ]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(sample)
    print(f"  ✓ Sample dataset generated: {filepath}\n")


# ─── Grade Logic ──────────────────────────────────────────────────────────────
def get_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "Merit"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"


# ─── Analysis Functions ───────────────────────────────────────────────────────
def section(title):
    print("\n" + "=" * 55)
    print(f"  {title}")
    print("=" * 55)


def divider():
    print("-" * 55)


def bar_chart(label, value, max_value, width=30, symbol="█"):
    """Print a simple text-based bar chart row."""
    filled = int((value / max_value) * width) if max_value > 0 else 0
    bar = symbol * filled
    print(f"  {label:<18} {bar:<30} {value:.1f}")


# ─── 1. Dataset Overview ──────────────────────────────────────────────────────
def dataset_overview(students):
    section("1. DATASET OVERVIEW")
    total = len(students)
    courses = set(s["course"] for s in students)
    genders = defaultdict(int)
    for s in students:
        genders[s.get("gender", "Unknown")] += 1

    print(f"  Total records   : {total}")
    print(f"  Courses covered : {len(courses)}")
    for course in sorted(courses):
        count = sum(1 for s in students if s["course"] == course)
        print(f"    • {course}: {count} students")
    print(f"\n  Gender breakdown:")
    for gender, count in sorted(genders.items()):
        print(f"    • {gender}: {count}")


# ─── 2. Marks Statistics ──────────────────────────────────────────────────────
def marks_statistics(students):
    section("2. MARKS STATISTICS")
    marks = [s["marks"] for s in students]
    print(f"  Mean (Average)  : {statistics.mean(marks):.2f}%")
    print(f"  Median          : {statistics.median(marks):.2f}%")
    print(f"  Std Deviation   : {statistics.stdev(marks):.2f}%")
    print(f"  Highest Mark    : {max(marks):.2f}%")
    print(f"  Lowest Mark     : {min(marks):.2f}%")
    print(f"  Range           : {max(marks) - min(marks):.2f}%")


# ─── 3. Grade Distribution ────────────────────────────────────────────────────
def grade_distribution(students):
    section("3. GRADE DISTRIBUTION")
    grade_counts = defaultdict(int)
    for s in students:
        grade_counts[get_grade(s["marks"])] += 1

    total = len(students)
    print(f"  {'Grade':<14} {'Count':<8} {'Percentage'}")
    divider()
    for grade in ["Distinction", "Merit", "Pass", "Fail"]:
        count = grade_counts[grade]
        pct = (count / total) * 100
        print(f"  {grade:<14} {count:<8} {pct:.1f}%")

    print("\n  Visual Distribution:")
    max_count = max(grade_counts.values())
    for grade in ["Distinction", "Merit", "Pass", "Fail"]:
        bar_chart(grade, grade_counts[grade], max_count)


# ─── 4. Course Comparison ─────────────────────────────────────────────────────
def course_comparison(students):
    section("4. COURSE PERFORMANCE COMPARISON")
    courses = defaultdict(list)
    for s in students:
        courses[s["course"]].append(s["marks"])

    print(f"  {'Course':<28} {'Avg':<8} {'Top':<8} {'Low':<8} {'Students'}")
    divider()
    for course, marks_list in sorted(courses.items()):
        avg = statistics.mean(marks_list)
        top = max(marks_list)
        low = min(marks_list)
        count = len(marks_list)
        print(f"  {course:<28} {avg:<8.1f} {top:<8.1f} {low:<8.1f} {count}")

    print("\n  Average marks by course (bar chart):")
    all_avgs = [statistics.mean(m) for m in courses.values()]
    max_avg = max(all_avgs)
    for course, marks_list in sorted(courses.items()):
        avg = statistics.mean(marks_list)
        bar_chart(course[:18], avg, 100)


# ─── 5. Top and Bottom Performers ─────────────────────────────────────────────
def top_and_bottom(students, n=5):
    section("5. TOP AND BOTTOM PERFORMERS")
    sorted_students = sorted(students, key=lambda s: s["marks"], reverse=True)

    print(f"  TOP {n} STUDENTS")
    divider()
    print(f"  {'Name':<25} {'Course':<28} {'Marks'}")
    divider()
    for s in sorted_students[:n]:
        print(f"  {s['name']:<25} {s['course']:<28} {s['marks']:.1f}%  ({get_grade(s['marks'])})")

    print(f"\n  BOTTOM {n} STUDENTS")
    divider()
    print(f"  {'Name':<25} {'Course':<28} {'Marks'}")
    divider()
    for s in sorted_students[-n:]:
        print(f"  {s['name']:<25} {s['course']:<28} {s['marks']:.1f}%  ({get_grade(s['marks'])})")


# ─── 6. Attendance vs Marks Insight ──────────────────────────────────────────
def attendance_insight(students):
    if "attendance" not in students[0]:
        return
    section("6. ATTENDANCE VS PERFORMANCE INSIGHT")

    high_att = [s for s in students if float(s.get("attendance", 0)) >= 80]
    low_att = [s for s in students if float(s.get("attendance", 0)) < 80]

    if high_att:
        avg_high = statistics.mean(s["marks"] for s in high_att)
    else:
        avg_high = 0

    if low_att:
        avg_low = statistics.mean(s["marks"] for s in low_att)
    else:
        avg_low = 0

    print(f"  Students with 80%+ attendance  : {len(high_att)} students, avg marks = {avg_high:.1f}%")
    print(f"  Students with under 80% attend  : {len(low_att)} students, avg marks = {avg_low:.1f}%")
    print(f"\n  Insight: Students with higher attendance scored {abs(avg_high - avg_low):.1f}% {'more' if avg_high > avg_low else 'less'} on average.")


# ─── 7. Key Insights Summary ─────────────────────────────────────────────────
def summary_insights(students):
    section("7. KEY INSIGHTS SUMMARY")
    marks = [s["marks"] for s in students]
    avg = statistics.mean(marks)
    pass_rate = sum(1 for s in students if s["marks"] >= 50) / len(students) * 100
    distinction_rate = sum(1 for s in students if s["marks"] >= 75) / len(students) * 100

    print(f"  ✔ The overall class average is {avg:.1f}%.")
    print(f"  ✔ {pass_rate:.1f}% of students achieved a passing grade (50%+).")
    print(f"  ✔ {distinction_rate:.1f}% of students achieved a distinction (75%+).")

    courses = defaultdict(list)
    for s in students:
        courses[s["course"]].append(s["marks"])
    best_course = max(courses, key=lambda c: statistics.mean(courses[c]))
    worst_course = min(courses, key=lambda c: statistics.mean(courses[c]))
    print(f"  ✔ Best performing course: {best_course} (avg: {statistics.mean(courses[best_course]):.1f}%)")
    print(f"  ✔ Needs improvement: {worst_course} (avg: {statistics.mean(courses[worst_course]):.1f}%)")


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    DATA_FILE = "student_data.csv"

    print("\n" + "=" * 55)
    print("  STUDENT PERFORMANCE DATA ANALYSIS")
    print("  Author: Awenkosi Moyo")
    print("=" * 55)

    # Generate sample data if no file exists
    if not os.path.exists(DATA_FILE):
        print(f"\n  No dataset found. Generating sample data...")
        generate_sample_data(DATA_FILE)

    students = load_data(DATA_FILE)

    if not students:
        print("  ✗ No valid student records found in dataset.")
        return

    print(f"\n  Loaded {len(students)} student records from '{DATA_FILE}'")

    dataset_overview(students)
    marks_statistics(students)
    grade_distribution(students)
    course_comparison(students)
    top_and_bottom(students, n=5)
    attendance_insight(students)
    summary_insights(students)

    print("\n" + "=" * 55)
    print("  ANALYSIS COMPLETE")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
