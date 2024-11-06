# File: common_data_csv.py
# Purpose: Demonstrate how to check for common data among multiple CSV files using pandas

import pandas as pd

# Create sample CSV files
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 22]
})
df1.to_csv('file1.csv', index=False)

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6, 7],
    'Name': ['Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo']
})
df2.to_csv('file2.csv', index=False)

df3 = pd.DataFrame({
    'ID': [1, 3, 5, 7, 9],
    'Name': ['Alice', 'Charlie', 'Eve', 'Grace', 'Ivy'],
    'Salary': [50000, 60000, 55000, 65000, 70000]
})
df3.to_csv('file3.csv', index=False)

# Read CSV files
file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')
file3 = pd.read_csv('file3.csv')

print("File 1:")
print(file1)
print("\nFile 2:")
print(file2)
print("\nFile 3:")
print(file3)
print("\n")

# Find common data based on 'ID' column
common_ids = set(file1['ID']) & set(file2['ID']) & set(file3['ID'])
print("Common IDs across all files:", common_ids)

# Find common data based on 'Name' column
common_names = set(file1['Name']) & set(file2['Name']) & set(file3['Name'])
print("Common Names across all files:", common_names)

# Get rows with common IDs from all files
common_data = pd.merge(pd.merge(file1, file2, on='ID'), file3, on='ID')
print("\nCommon data across all files based on ID:")
print(common_data)

# This script demonstrates how to:
# 1. Create sample CSV files
# 2. Read multiple CSV files using pandas
# 3. Find common elements across multiple DataFrames
# 4. Merge DataFrames based on common columns
#
# Users can modify this script to work with their own CSV files and
# explore different ways of finding common data among them.
