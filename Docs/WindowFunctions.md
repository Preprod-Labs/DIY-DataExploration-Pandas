# Window Functions in Pandas

This script demonstrates how to use operations similar to SQL window functions in pandas.

## Code Breakdown:

1. **Creating a Sample DataFrame:**
   ```python
   data = {
       'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
       'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
       'Salary': [75000, 65000, 80000, 70000, 68000, 72000, 71000, 67000]
   }
   df = pd.DataFrame(data)
   ```

2. **Ranking Employees:**
   ```python
   df['Salary_Rank'] = df.groupby('Department')['Salary'].rank(method='dense', ascending=False)
   ```
   This ranks employees within each department based on salary.

3. **Cumulative Sum:**
   ```python
   df['Cumulative_Salary'] = df.groupby('Department')['Salary'].cumsum()
   ```
   This calculates the running total of salaries within each department.

4. **Difference from Average:**
   ```python
   df['Salary_Diff_From_Avg'] = df['Salary'] - df.groupby('Department')['Salary'].transform('mean')
   ```
   This calculates how much each salary differs from the department average.

5. **Row Numbering:**
   ```python
   df['Row_Number'] = df.groupby('Department').cumcount() + 1
   ```
   This assigns a sequential number to each row within its department.

## Key Takeaways:

- Use `rank()` for ranking within groups
- Use `cumsum()` for cumulative calculations
- Use `transform()` to apply a function to each group
- Use `cumcount()` for row numbering within groups
- These operations allow for complex analytical queries similar to SQL window functions
