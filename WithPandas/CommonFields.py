# File: common_data_csv.py
# Purpose: Demonstrate how to check for common data among multiple CSV files using pandas

# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Version      : V 1.0
#   Unit test    : Pass
#   Integration test: Pass
#   Description  : This script creates sample CSV files and demonstrates how to read them using pandas.
#                  It checks for common data among the CSV files based on specific columns and merges
#                  the DataFrames to find common rows.
# numpy==2.1.1
# pandas==2.2.2
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd  # Importing pandas library for data manipulation and analysis

# --------------------------------------------------------------------------------------
# Step 1: Create sample CSV files
# --------------------------------------------------------------------------------------
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],  # Unique identifier
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],  # Names of individuals
    'Age': [25, 30, 35, 28, 22]  # Ages of individuals
})
df1.to_csv('file1.csv', index=False)  # Saving DataFrame to CSV file

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6, 7],  # Unique identifier
    'Name': ['Charlie', 'David', 'Eve', 'Frank', 'Grace'],  # Names of individuals
    'City': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo']  # Cities of individuals
})
df2.to_csv('file2.csv', index=False)  # Saving DataFrame to CSV file

df3 = pd.DataFrame({
    'ID': [1, 3, 5, 7, 9],  # Unique identifier
    'Name': ['Alice', 'Charlie', 'Eve', 'Grace', 'Ivy'],  # Names of individuals
    'Salary': [50000, 60000, 55000, 65000, 70000]  # Salaries of individuals
})
df3.to_csv('file3.csv', index=False)  # Saving DataFrame to CSV file

# --------------------------------------------------------------------------------------
# Step 2: Read CSV files
# --------------------------------------------------------------------------------------
file1 = pd.read_csv('file1.csv')  # Reading the first CSV file
file2 = pd.read_csv('file2.csv')  # Reading the second CSV file
file3 = pd.read_csv('file3.csv')  # Reading the third CSV file

# Display the contents of each file
print("File 1:")
print(file1)
print("\nFile 2:")
print(file2)
print("\nFile 3:")
print(file3)
print("\n")

# --------------------------------------------------------------------------------------
# Step 3: Find common data based on specific columns
# --------------------------------------------------------------------------------------

# Find common IDs across all files
common_ids = set(file1['ID']) & set(file2['ID']) & set(file3['ID'])
print("Common IDs across all files:", common_ids)

# Find common Names across all files
common_names = set(file1['Name']) & set(file2['Name']) & set(file3['Name'])
print("Common Names across all files:", common_names)

# --------------------------------------------------------------------------------------
# Step 4: Merge DataFrames based on common columns
# --------------------------------------------------------------------------------------

# Get rows with common IDs from all files
common_data = pd.merge(pd.merge(file1, file2, on='ID'), file3, on='ID')
print("\nCommon data across all files based on ID:")
print(common_data)

# --------------------------------------------------------------------------------------
# End of Script
# --------------------------------------------------------------------------------------

# SUMMARY:
# This script demonstrates how to:
# 1. Create sample CSV files.
# 2. Read multiple CSV files using pandas.
# 3. Find common elements across multiple DataFrames based on specific columns.
# 4. Merge DataFrames to find common rows based on common columns.
#
# USERS:
# Users can modify the sample data and file paths to work with their own CSV files.
# They can also explore different ways of finding common data among multiple files.
