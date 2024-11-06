# Data Selection in Pandas

This script demonstrates various ways to select data from a pandas DataFrame.

## Code Breakdown:

1. **Creating a DataFrame:**
   ```python
   data = {
       'Name': ['Alice', 'Bob', 'Charlie', 'David'],
       'Age': [25, 30, 35, 28],
       'City': ['New York', 'San Francisco', 'London', 'Paris'],
       'Salary': [50000, 75000, 80000, 65000]
   }
   df = pd.DataFrame(data)
   ```
   This creates a table with columns for Name, Age, City, and Salary.

2. **Selecting Columns:**
   - Using column names:
     ```python
     selected_columns = df[['Name', 'Age']]
     ```
   - Using `loc` accessor:
     ```python
     selected_columns = df.loc[:, ['Name', 'Salary']]
     ```
   - Using `iloc` accessor:
     ```python
     selected_columns = df.iloc[:, [0, 2]]
     ```

3. **Filtering Data:**
   ```python
   high_salary = df[df['Salary'] > 70000][['Name', 'Salary']]
   ```
   This selects employees with a salary greater than 70000.

## Key Takeaways:

- Use `[]` for simple column selection
- Use `loc[]` for label-based selection
- Use `iloc[]` for position-based selection
- Combine conditions and column selection for filtering
