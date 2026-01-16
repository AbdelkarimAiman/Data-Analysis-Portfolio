import numpy as np

"""
Scenario: 2D Matrix Analysis (Students x Subjects).
Key Concept: Understanding Axis 0 (Columns) vs Axis 1 (Rows).
"""

# 1. Setup Data
# Rows = Students (Student A, B, C, D)
# Columns = Subjects (Math, Physics, English)
scores = np.array([
    [80, 85, 90],  # Student A
    [70, 75, 78],  # Student B
    [88, 92, 95],  # Student C
    [60, 65, 70]   # Student D
])

subjects = ["Math", "Physics", "English"]
students = ["Student A", "Student B", "Student C", "Student D"]

print(f"---  Exam Matrix Analysis ---\n")
print(f"Matrix Shape: {scores.shape} (4 Students, 3 Subjects)\n")

# 2. Row-wise Analysis (Axis 1)
# "Collapse the columns to get one number per row"
student_avg = scores.mean(axis=1)

print(" Performance per Student (Axis 1):")
for name, avg in zip(students, student_avg):
    print(f"   • {name}: {avg:.2f}")

print("-" * 30)

# 3. Column-wise Analysis (Axis 0)
# "Collapse the rows to get one number per column"
subject_avg = scores.mean(axis=0)

print(" Difficulty per Subject (Axis 0):")
for subject, avg in zip(subjects, subject_avg):
    print(f"   • {subject}: {avg:.2f}")

# 4. Advanced: Who got the highest score in Physics? (Column index 1)
physics_scores = scores[:, 1] # Slicing: All rows, Column 1
best_student_idx = np.argmax(physics_scores)
print(f"\n Top in Physics: {students[best_student_idx]} ({physics_scores[best_student_idx]})")