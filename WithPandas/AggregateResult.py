# File: aggregate_results.py
# Purpose: Demonstrate how to perform aggregation operations (sum, avg, max, min) using pandas

# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Developer details:
#   Name         : Lay Sheth and Rishav Raj
#   Role         : Software Engineers
#   Version      : V 1.0
#   Unit test    : Pass
#   Integration test: Pass
#   Description  : This script creates a sample DataFrame and performs various aggregation
#                  operations such as sum, average, maximum, and minimum grouped by categories.
#                  It also demonstrates how to apply multiple aggregations on different columns.
#                  Users can modify the DataFrame and aggregation functions to suit their data analysis needs.
#
#numpy==2.1.1
#pandas==2.2.2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd  # Importing pandas library for data manipulation and analysis

# --------------------------------------------------------------------------------------
# Step 1: Create a sample DataFrame
# --------------------------------------------------------------------------------------
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],  # Category labels
    'Value1': [10, 15, 20, 25, 30, 35, 40, 45],           # Numeric values for Value1
    'Value2': [100, 150, 200, 250, 300, 350, 400, 450]    # Numeric values for Value2
}
df = pd.DataFrame(data)  # Creating the DataFrame with the provided data

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")  # Adding a newline for better readability in the output

# --------------------------------------------------------------------------------------
# Step 2: Perform aggregation operations grouped by 'Category'
# --------------------------------------------------------------------------------------

# 1. Sum of numeric columns grouped by 'Category'
sum_results = df.groupby('Category').sum()
print("Sum of values by category:")
print(sum_results)
print("\n")

# 2. Average (Mean) of numeric columns grouped by 'Category'
avg_results = df.groupby('Category').mean()
print("Average of values by category:")
print(avg_results)
print("\n")

# 3. Maximum values of numeric columns grouped by 'Category'
max_results = df.groupby('Category').max()
print("Maximum values by category:")
print(max_results)
print("\n")

# 4. Minimum values of numeric columns grouped by 'Category'
min_results = df.groupby('Category').min()
print("Minimum values by category:")
print(min_results)
print("\n")

# 5. Multiple aggregations on different columns
#    Applying sum, mean, max, and min to both 'Value1' and 'Value2'
multi_agg = df.groupby('Category').agg({
    'Value1': ['sum', 'mean', 'max', 'min'],  # Aggregations for Value1
    'Value2': ['sum', 'mean', 'max', 'min']   # Aggregations for Value2
})
print("Multiple aggregations by category:")
print(multi_agg)

# --------------------------------------------------------------------------------------
# End of Script
# --------------------------------------------------------------------------------------

# SUMMARY:
# This script demonstrates how to:
# 1. Group data by a specific column ('Category').
# 2. Perform various aggregation operations (sum, average, max, min) on grouped data.
# 3. Apply multiple aggregations to different columns simultaneously.
#
# USERS:
# Users can modify the 'data' dictionary to include their own datasets.
# They can also customize the aggregation functions in the 'agg' method
# to perform other operations as needed for their data analysis tasks.
