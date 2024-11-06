# Finding Common Data in Multiple CSV Files

This script demonstrates how to find common data among multiple CSV files using pandas.

## Code Breakdown:

1. **Creating Sample CSV Files:**
   ```python
   df1 = pd.DataFrame({
       'ID': [1, 2, 3, 4, 5],
       'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
       'Age': [25, 30, 35, 28, 22]
   })
   df1.to_csv('file1.csv', index=False)
   ```
   Similar code creates file2.csv and file3.csv with different data.

2. **Reading CSV Files:**
   ```python
   file1 = pd.read_csv('file1.csv')
   file2 = pd.read_csv('file2.csv')
   file3 = pd.read_csv('file3.csv')
   ```

3. **Finding Common Data:**
   - Common IDs:
     ```python
     common_ids = set(file1['ID']) & set(file2['ID']) & set(file3['ID'])
     ```
   - Common Names:
     ```python
     common_names = set(file1['Name']) & set(file2['Name']) & set(file3['Name'])
     ```

4. **Merging Common Data:**
   ```python
   common_data = pd.merge(pd.merge(file1, file2, on='ID'), file3, on='ID')
   ```

## Key Takeaways:

- Use `pd.read_csv()` to read CSV files
- Use set operations to find common elements
- Use `pd.merge()` to combine data based on common columns
- This approach is useful for data integration and comparison across multiple sources
