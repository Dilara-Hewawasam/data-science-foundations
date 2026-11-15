import pandas as pd


# Table 1: Student Profiles
students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amal", "Binu", "Chamari", "Dinuka", "Erandi"],
    "Dept_Code": ["CS", "STAT", "MATH", "CS", "STAT"]
})

# Table 2: Semester Exam Scores (Notice 105 is missing, and 106 is an extra transfer student)
scores = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 106],
    "Midterm": [78, 88, 65, 92, 81],
    "Final": [84, 91, 70, 95, 85]
})

# Table 3: Department Metadata
departments = pd.DataFrame({
    "Dept_Code": ["CS", "STAT", "MATH"],
    "Dept_Name": ["Computer Science", "Statistics", "Applied Mathematics"],
    "Faculty_Building": ["Block A", "Block C", "Block B"]
})

# --- TASK 1: Inner Merge ---
inner_merged = pd.merge(students, scores, on="Student_ID", how="inner")
print("--- Task 1: Inner Merge ---")
print(inner_merged, "\n")

# --- TASK 2: Left Merge ---
student_records = pd.merge(students, scores, on="Student_ID", how="left")
print("--- Task 2: Left Merge ---")
print(student_records, "\n")

# --- TASK 3: Chained Merge ---
student_records = pd.merge(student_records, departments, on="Dept_Code", how="left")
print("--- Task 3: Chained Merge with Department Info ---")
print(student_records, "\n")

# --- TASK 4: Pivot Table ---
dept_summary = pd.pivot_table(
    student_records,
    values=["Midterm", "Final"],
    index="Dept_Name",
    aggfunc="mean"
)
print("--- Task 4: Department Pivot Summary ---")
print(dept_summary)