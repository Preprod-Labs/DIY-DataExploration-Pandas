# File: aggregate_results.py
# Purpose: Demonstrate how to perform aggregation operations (sum, avg, max, min) using pandas

import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],
    'Value1': [10, 15, 20, 25, 30, 35, 40, 45],
    'Value2': [100, 150, 200, 250, 300, 350, 400, 450]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# Perform aggregation operations

# 1. Sum
sum_results = df.groupby('Category').sum()
print("Sum of values by category:")
print(sum_results)
print("\n")

# 2. Average (Mean)
avg_results = df.groupby('Category').mean()
print("Average of values by category:")
print(avg_results)
print("\n")

# 3. Maximum
max_results = df.groupby('Category').max()
print("Maximum values by category:")
print(max_results)
print("\n")

# 4. Minimum
min_results = df.groupby('Category').min()
print("Minimum values by category:")
print(min_results)
print("\n")

# 5. Multiple aggregations
multi_agg = df.groupby('Category').agg({
    'Value1': ['sum', 'mean', 'max', 'min'],
    'Value2': ['sum', 'mean', 'max', 'min']
})
print("Multiple aggregations by category:")
print(multi_agg)

# This script demonstrates how to:
# 1. Group data by a specific column
# 2. Perform various aggregation operations (sum, average, max, min)
# 3. Apply multiple aggregations to different columns
#
# Users can modify this script to work with their own data and
# explore different aggregation techniques to gain insights from their datasets.
