# File: join_tables.py
# Purpose: Demonstrate different types of joins using pandas

import pandas as pd

# Create two sample DataFrames
df1 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'department': ['HR', 'IT', 'Finance', 'Marketing', 'IT']
})

df2 = pd.DataFrame({
    'employee_id': [2, 3, 4, 6, 7],
    'salary': [50000, 60000, 55000, 65000, 70000],
    'bonus': [5000, 7000, 5500, 6500, 7500]
})

print("DataFrame 1 (Employees):")
print(df1)
print("\nDataFrame 2 (Salaries):")
print(df2)
print("\n")

# Inner Join
inner_join = pd.merge(df1, df2, on='employee_id', how='inner')
print("Inner Join:")
print(inner_join)
print("\n")

# Left Join
left_join = pd.merge(df1, df2, on='employee_id', how='left')
print("Left Join:")
print(left_join)
print("\n")

# Right Join
right_join = pd.merge(df1, df2, on='employee_id', how='right')
print("Right Join:")
print(right_join)
print("\n")

# Outer Join
outer_join = pd.merge(df1, df2, on='employee_id', how='outer')
print("Outer Join:")
print(outer_join)

# This file demonstrates various types of joins in pandas:
# 1. Inner Join: Returns only the rows that have matching values in both DataFrames
# 2. Left Join: Returns all rows from the left DataFrame and matching rows from the right DataFrame
# 3. Right Join: Returns all rows from the right DataFrame and matching rows from the left DataFrame
# 4. Outer Join: Returns all rows when there's a match in either DataFrame
#
# Users can experiment with different join types to understand how they work with their own data.
