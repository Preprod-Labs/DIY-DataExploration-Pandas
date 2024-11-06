# Data Exploration with Pandas - Info File

This guide explains various data exploration techniques using pandas in simple language for beginners.

## Concepts Covered:

1. Data Selection
2. Table Joins
3. Common Fields in CSV Files
4. Aggregating Results
5. Window Functions

## How the Code Works:

Each script follows a similar pattern:
1. Import pandas
2. Create or load sample data
3. Perform operations on the data
4. Display results

## Key Functions and Their Purpose:

- `pd.DataFrame()`: Creates a table-like structure to hold data
- `df[['column1', 'column2']]`: Selects specific columns
- `df.loc[]`: Selects data by label
- `df.iloc[]`: Selects data by position
- `pd.merge()`: Combines two DataFrames
- `df.groupby()`: Groups data for aggregation
- `df.agg()`: Performs multiple aggregations
- `df.rank()`: Assigns ranks within groups
- `df.cumsum()`: Calculates cumulative sum

## GPT Prompts for Understanding:

1. Explain the difference between `loc` and `iloc` in pandas.
2. How does an inner join differ from an outer join?
3. What's the purpose of the `groupby()` function in pandas?
4. Describe a real-world scenario where you might use a left join.
5. How can you find common elements between two pandas Series?
6. Explain the concept of window functions and their uses.
7. What's the difference between `sum()` and `cumsum()` in pandas?
8. How would you calculate the average salary by department?
9. Explain the purpose of the `rank()` function in pandas.
10. How can you filter a DataFrame based on a condition?

These prompts will help users deepen their understanding of the code and concepts presented.
