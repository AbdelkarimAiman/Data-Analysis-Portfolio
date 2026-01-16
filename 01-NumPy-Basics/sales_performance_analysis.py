import numpy as np

"""
Scenario: Weekly Store Sales Analysis.
Techniques: Boolean Indexing, Argmax, and Broadcasting (Vectorized Operations).
"""

# 1. Data Setup
# It's crucial to map data to labels (Days of the week)
daily_sales = np.array([120, 150, 170, 90, 200, 180, 160])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

print(f"---  Weekly Sales Report ---\n")

# 2. Basic Metrics (KPIs)
total_revenue = np.sum(daily_sales)
avg_daily_sales = np.mean(daily_sales)

print(f" Total Revenue:    ${total_revenue}")
print(f" Average Daily:    ${avg_daily_sales:.2f}")

# 3. Advanced: Identifying Best Performing Day
# np.argmax returns the *index* of the maximum value
best_day_index = np.argmax(daily_sales)
best_day = days[best_day_index]
highest_value = daily_sales[best_day_index]

print(f" Best Sales Day:   {best_day} (${highest_value})")

# 4. Advanced: Filtering (Which days performed above target?)
# Let's say 'High Performance' is anything above $160
target_threshold = 160

# Boolean Mask (True/False list)
high_sales_mask = daily_sales > target_threshold

# Apply mask to BOTH sales array AND days array
high_sales_values = daily_sales[high_sales_mask]
high_sales_days = days[high_sales_mask]

print(f"\n High Performance Days (>{target_threshold}):")
# Zip creates pairs like (Wed, 170), (Fri, 200)...
for day, value in zip(high_sales_days, high_sales_values):
    print(f"   • {day}: ${value}")

# 5. Business Insight: Deviation from Average
# How much did each day differ from the weekly average?
# NumPy allows subtracting a scalar (avg) from the whole array at once!
variance = daily_sales - avg_daily_sales

print(f"\n Deviation from Average (Trend):")
print(f"   {variance}") 
# Positive means above average, Negative means below average