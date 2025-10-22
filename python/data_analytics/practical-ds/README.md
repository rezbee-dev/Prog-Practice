# Practical Data Science with Python

- By: Nathan George


## Pandas basic notes

<details><summary>1) How to view the first `n` rows in a dataframe?</summary>

- `.head(n)`
</details>

<details><summary>2) What's a good way to represent data with a lot of columns?</summary>

- switch columns with rows, using transpose
- ex: `sql_df.head().T`
</details>

<details><summary>3) How do you view the number of rows and columns in a dataframe?</summary>

- `print(<df>.shape)`
</details>

<details><summary>4) How do you view the datatypes, column names, memory usage, and non-null count of a dataframe?</summary>

- `<df>.info()`
</details>

<details><summary>5) How do you find the number of missing values (or values with `NaN`) for each column in data frame?</summary>

- `<df>.isna().sum()`
</details>

<details><summary>6) How do you display the most frequent value for non-numeric columns?</summary>

- `<df>[<column>].mode()`
- Ex: `itunes_df['Genre'].mode()`
</details>

<details><summary>7) How do you find the number of times unique values appear in a column?</summary>

- `<df>[<column>].value_counts()`
- Ex: `itunes_df['Genre'].value_counts()`
</details>

<details><summary>8) How do you find the top five most frequent unique values that appear in a column?</summary>

- `<df>[<column>].value_counts()[:5]`
- Ex: `itunes_df['Genre'].value_counts()[:5]`
</details>

<details><summary>9) How do you how many total unique items there are for a column?</summary>

- `<df>[<column>].unique().shape`
- Ex: `itunes_df['Genre'].unique().shape`
</details>

<details><summary>10) How do you how many total unique items there are for a column?</summary>

- `<df>[<column>].unique().shape`
- Ex: `itunes_df['Genre'].unique().shape`
</details>

<details><summary>10) What is the Pearson Correlation, and how do you calculate it for a dataframe?</summary>

- Measures how linearly correlated two datasets are
  - -1 (inverse correlation), to 0 (no correlation), to +1 (perfect linear correlation)
  - `<df>.corr()`
</details>