# File: select_columns.py
# Purpose: Demonstrate how to select certain columns from a DataFrame using pandas

# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Developer details:
#   Name         : Lay Sheth and Rishav Raj
#   Role         : Software Engineers
#   Version      : V 1.0
#   Unit test    : Pass
#   Integration test: Pass
#   Description  : This script creates a sample DataFrame and demonstrates various methods to select
#                  specific columns from the DataFrame using pandas. It also shows how to select
#                  columns based on conditions.
# numpy==2.1.1
# pandas==2.2.2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd  # Importing pandas library for data manipulation and analysis

# --------------------------------------------------------------------------------------
# Step 1: Create a sample DataFrame
# --------------------------------------------------------------------------------------
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],  # Names of individuals
    'Age': [25, 30, 35, 28],  # Ages of individuals
    'City': ['New York', 'San Francisco', 'London', 'Paris'],  # Cities of individuals
    'Salary': [50000, 75000, 80000, 65000]  # Salaries of individuals
}

df = pd.DataFrame(data)  # Creating the DataFrame with the provided data

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")  # Adding a newline for better readability in the output

# --------------------------------------------------------------------------------------
# Step 2: Select specific columns using different methods
# --------------------------------------------------------------------------------------

# Method 1: Using column names in square brackets
selected_columns = df[['Name', 'Age']]
print("Selected columns (Method 1):")
print(selected_columns)
print("\n")

# Method 2: Using loc accessor
selected_columns = df.loc[:, ['Name', 'Salary']] # " : " indicates select all rows
print("Selected columns (Method 2):")
print(selected_columns)
print("\n")

# Method 3: Using iloc accessor (by column index)
selected_columns = df.iloc[:, [0, 2]]
print("Selected columns (Method 3):")
print(selected_columns)
print("\n")

# --------------------------------------------------------------------------------------
# Step 3: Selecting columns based on a condition
# --------------------------------------------------------------------------------------

# Select rows where Salary is greater than 70000
high_salary = df[df['Salary'] > 70000][['Name', 'Salary']]
print("Employees with high salary:")
print(high_salary)

# --------------------------------------------------------------------------------------
# End of Script
# --------------------------------------------------------------------------------------

# SUMMARY:
# This script demonstrates various ways to select columns from a pandas DataFrame:
# 1. Using column names in square brackets.
# 2. Using the loc accessor.
# 3. Using the iloc accessor by column index.
# 4. Selecting columns based on a condition.
#
# USERS:
# Users can experiment with different selection methods and conditions to extract
# the desired information from their data.
