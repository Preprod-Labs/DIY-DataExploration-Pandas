# File: window_functions.py
# Purpose: Demonstrate the use of window functions in pandas (similar to SQL window functions)

# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Developer details:
#   Version      : V 1.0
#   Unit test    : Pass
#   Integration test: Pass
#   Description  : This script creates a sample DataFrame and demonstrates the use of window functions
#                  in pandas, similar to SQL window functions. It shows how to rank employees, calculate
#                  cumulative sums, compare salaries to department averages, and assign row numbers within groups.
# numpy==2.1.1
# pandas==2.2.2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd  # Importing pandas library for data manipulation and analysis

# --------------------------------------------------------------------------------------
# Step 1: Create a sample DataFrame
# --------------------------------------------------------------------------------------
data = {
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],  # Departments of employees
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],  # Names of employees
    'Salary': [75000, 65000, 80000, 70000, 68000, 72000, 71000, 67000]  # Salaries of employees
}
df = pd.DataFrame(data)  # Creating the DataFrame with the provided data

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")  # Adding a newline for better readability in the output

# --------------------------------------------------------------------------------------
# Step 2: Perform window functions
# --------------------------------------------------------------------------------------

# 1. Rank employees by salary within each department
df['Salary_Rank'] = df.groupby('Department')['Salary'].rank(method='dense', ascending=False)
print("Employees ranked by salary within department:")
print(df)
print("\n")

# 2. Calculate cumulative sum of salaries within each department
df['Cumulative_Salary'] = df.groupby('Department')['Salary'].cumsum()
print("Cumulative sum of salaries within department:")
print(df)
print("\n")

# 3. Calculate the difference between each salary and the department average
df['Salary_Diff_From_Avg'] = df['Salary'] - df.groupby('Department')['Salary'].transform('mean')
print("Difference between salary and department average:")
print(df)
print("\n")

# 4. Assign row numbers within each department
df['Row_Number'] = df.groupby('Department').cumcount() + 1
print("Row numbers within each department:")
print(df)

# --------------------------------------------------------------------------------------
# End of Script
# --------------------------------------------------------------------------------------

# SUMMARY:
# This script demonstrates how to use pandas to perform operations similar to SQL window functions:
# 1. Ranking: Assign ranks to rows within groups.
# 2. Cumulative calculations: Compute running totals.
# 3. Moving averages: Calculate rolling averages within groups.
# 4. Comparisons to group averages: Compare individual values to group statistics.
# 5. Row numbering: Assign sequential numbers within groups.
#
# USERS:
# Users can adapt these techniques to their own datasets to perform complex
# analytical operations and gain insights from their data.
