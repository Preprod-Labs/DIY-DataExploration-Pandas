# Data Exploration with Pandas

## Overview

This project is a comprehensive guide to data exploration techniques using Pandas, a powerful data manipulation library in Python. It's designed to help both beginners and intermediate users enhance their data analysis skills through practical examples and clear explanations.

To Learn more about the project using your favorite LLM, click [Here](prompts.md)

## Table of Contents

1. [Features](#features)
2. [Documentation](#documentation)
3. [Installation](#installation)
4. [Usage](#usage)

## Features

This project covers a wide range of data exploration techniques, including:

- **Data Selection**: Various methods to select and filter data from DataFrames
- **Table Joins**: Different types of joins to combine data from multiple sources
- **Common Fields Analysis**: Techniques to identify and work with shared data across multiple CSV files
- **Aggregation**: Performing summary statistics and grouping operations
- **Window Functions**: Implementing SQL-like window functions for advanced analytics

Each feature is demonstrated through Python scripts and explained in detail in the accompanying documentation.

## Documentation

Detailed explanations for each concept are available in the `Docs` folder:

- [Data Selection Guide](Docs/DataSelection.md)
- [Table Joins Explained](Docs/TableJoin.md)
- [Working with Common Fields](Docs/CommonFields.md)
- [Aggregating Results](Docs/AggregateResults.md)
- [Window Functions in Pandas](Docs/WindowFunctions.md)

These documents provide in-depth explanations, code breakdowns, and key takeaways for each topic.

## Installation

To use this project, follow these steps to set up your environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/Preprod-Labs/DIY-DataExploration-Pandas.git
   ```

2. Create a virtual environment. If using Conda:
   ```
   conda create -n *env_name* python==3.12.0 -y
   conda activate *env_name*
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

After installation, you can run each script individually to see demonstrations and outputs:

1. Ensure your virtual environment is activated.

2. Navigate to the `WithPandas` folder:
   ```
   cd WithPandas
   ```

2. Run a script using Python:
   ```
   python DataSelection.py
   ```

3. View the output in your console.

4. Refer to the corresponding markdown file in the `Docs` folder for detailed explanations of the concepts demonstrated in each script.