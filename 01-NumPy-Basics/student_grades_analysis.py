import numpy as np

"""
Scenario: Analyzing student performance using NumPy.
Demonstrates: Basic Statistics, Aggregation, and Boolean Indexing (Filtering).
"""

# 1. Data Preparation
# Using integer type for precision
grades = np.array([85, 78, 92, 88, 76, 95, 89, 60, 100], dtype=int)

print(f"--- Class Performance Analysis ---")
print(f"Total Students: {len(grades)}")
print(f"All Grades: {grades}\n")

# 2. Basic Statistics (Aggregation)
# Using f-strings for cleaner output (formatting to 2 decimal places)
average_score = np.mean(grades)
median_score = np.median(grades)  # Good for detecting outliers
std_dev = np.std(grades)          # Shows how spread out the grades are

print(f" Statistics:")
print(f"• Average (Mean): {average_score:.2f}")
print(f"• Median Score:   {median_score}")
print(f"• Highest Score:  {np.max(grades)}")
print(f"• Lowest Score:   {np.min(grades)}")
print(f"• Std Deviation:  {std_dev:.2f}") # Low std dev = students have similar levels

# 3. Advanced: Filtering & Vectorization (The Power of NumPy!)
# Get grades above 90 without using a loop
top_performers = grades[grades >= 90]

print(f"\n Top Performers (>= 90):")
print(f"• Count: {len(top_performers)}")
print(f"• Scores: {top_performers}")

# 4. Bonus: Curve the grades (Add 5 bonus points to everyone)
curved_grades = grades + 5
print(f"\n Grades after 5-point Bonus:\n{curved_grades}")