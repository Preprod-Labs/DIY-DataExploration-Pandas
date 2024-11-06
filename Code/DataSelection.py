# File: select_columns.py
# Purpose: Demonstrate how to select certain columns from a DataFrame using pandas

import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'San Francisco', 'London', 'Paris'],
    'Salary': [50000, 75000, 80000, 65000]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Select specific columns
# Method 1: Using column names in square brackets
selected_columns = df[['Name', 'Age']]
print("Selected columns (Method 1):")
print(selected_columns)
print("\n")

# Method 2: Using loc accessor
selected_columns = df.loc[:, ['Name', 'Salary']]
print("Selected columns (Method 2):")
print(selected_columns)
print("\n")

# Method 3: Using iloc accessor (by column index)
selected_columns = df.iloc[:, [0, 2]]
print("Selected columns (Method 3):")
print(selected_columns)
print("\n")

# Selecting columns based on a condition
high_salary = df[df['Salary'] > 70000][['Name', 'Salary']]
print("Employees with high salary:")
print(high_salary)

# This file demonstrates various ways to select columns from a pandas DataFrame.
# Users can experiment with different selection methods and conditions to
# extract the desired information from their data.
