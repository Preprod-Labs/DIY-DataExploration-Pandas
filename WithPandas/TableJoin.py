# File: join_tables.py
# Purpose: Demonstrate different types of joins using pandas

# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Developer details:
#   Name         : Lay Sheth and Rishav Raj
#   Role         : Software Engineers
#   Version      : V 1.0
#   Unit test    : Pass
#   Integration test: Pass
#   Description  : This script creates two sample DataFrames and demonstrates various types of joins
#                  (inner, left, right, outer) using pandas. It shows how to merge DataFrames based
#                  on a common column and explains the differences between each join type.
# numpy==2.1.1
# pandas==2.2.2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd  # Importing pandas library for data manipulation and analysis

# --------------------------------------------------------------------------------------
# Step 1: Create two sample DataFrames
# --------------------------------------------------------------------------------------
df1 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],  # Unique identifier for employees
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],  # Names of employees
    'department': ['HR', 'IT', 'Finance', 'Marketing', 'IT']  # Departments of employees
})

df2 = pd.DataFrame({
    'employee_id': [2, 3, 4, 6, 7],  # Unique identifier for employees
    'salary': [50000, 60000, 55000, 65000, 70000],  # Salaries of employees
    'bonus': [5000, 7000, 5500, 6500, 7500]  # Bonuses of employees
})

# Display the contents of each DataFrame
print("DataFrame 1 (Employees):")
print(df1)
print("\nDataFrame 2 (Salaries):")
print(df2)
print("\n")

# --------------------------------------------------------------------------------------
# Step 2: Perform different types of joins
# --------------------------------------------------------------------------------------

# Inner Join: Returns only the rows that have matching values in both DataFrames
inner_join = pd.merge(df1, df2, on='employee_id', how='inner')
print("Inner Join:")
print(inner_join)
print("\n")

# Left Join: Returns all rows from the left DataFrame and matching rows from the right DataFrame
left_join = pd.merge(df1, df2, on='employee_id', how='left')
print("Left Join:")
print(left_join)
print("\n")

# Right Join: Returns all rows from the right DataFrame and matching rows from the left DataFrame
right_join = pd.merge(df1, df2, on='employee_id', how='right')
print("Right Join:")
print(right_join)
print("\n")

# Outer Join: Returns all rows when there's a match in either DataFrame
outer_join = pd.merge(df1, df2, on='employee_id', how='outer')
print("Outer Join:")
print(outer_join)

# --------------------------------------------------------------------------------------
# End of Script
# --------------------------------------------------------------------------------------

# SUMMARY:
# This script demonstrates various types of joins in pandas:
# 1. Inner Join: Returns only the rows that have matching values in both DataFrames.
# 2. Left Join: Returns all rows from the left DataFrame and matching rows from the right DataFrame.
# 3. Right Join: Returns all rows from the right DataFrame and matching rows from the left DataFrame.
# 4. Outer Join: Returns all rows when there's a match in either DataFrame.
#
# USERS:
# Users can experiment with different join types to understand how they work with their own data.
