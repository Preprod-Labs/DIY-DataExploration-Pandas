# Table Joins in Pandas

This script demonstrates different types of joins using pandas, similar to SQL joins.

## Code Breakdown:

1. **Creating Sample DataFrames:**
   ```python
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
   ```
   This creates two tables: one with employee info and another with salary info.

2. **Performing Joins:**
   - Inner Join:
     ```python
     inner_join = pd.merge(df1, df2, on='employee_id', how='inner')
     ```
     Keeps only rows with matching employee_id in both tables.

   - Left Join:
     ```python
     left_join = pd.merge(df1, df2, on='employee_id', how='left')
     ```
     Keeps all rows from df1, and matching rows from df2.

   - Right Join:
     ```python
     right_join = pd.merge(df1, df2, on='employee_id', how='right')
     ```
     Keeps all rows from df2, and matching rows from df1.

   - Outer Join:
     ```python
     outer_join = pd.merge(df1, df2, on='employee_id', how='outer')
     ```
     Keeps all rows from both tables, filling with NaN where there's no match.

## Key Takeaways:

- Use `pd.merge()` for joining DataFrames
- The `on` parameter specifies the column to join on
- The `how` parameter determines the type of join
- Different joins are useful for different data analysis scenarios
