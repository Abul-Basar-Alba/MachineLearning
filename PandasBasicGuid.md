
# 📊 Complete Pandas Guide (Bangla + Resource Analysis)

---

## ✅ 1. Pandas Introduction

**Pandas** হলো একটি Python library যা ডেটা analysis, manipulation এবং cleaning নিয়ে এর জন্য অন্য ওপটিম টুল গুলিচ্ছে ইবার কাজ করায়।

---

## 🔄 2. Key Pandas Data Structures

### ✅ DataFrame:

* 2D tabular data (like Excel)
* Row & Column

```python
import pandas as pd

# Simple DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
})
```

### ✅ Series:

* 1D array (column-like)

```python
s = pd.Series([1, 2, 3])
```

---

## 📃 3. Creating DataFrame (Different Ways)

```python
# From dictionary
pd.DataFrame({"A": [1, 2], "B": [3, 4]})

# From list of lists
pd.DataFrame([[1, 2], [3, 4]], columns=["X", "Y"])

# From CSV
pd.read_csv("file.csv")
```

---

## ⚡ 4. Basic Operations

```python
# View data
print(df.head())    # First 5 rows
print(df.tail())    # Last 5 rows

# Column access
print(df["Name"])

# Row access
print(df.loc[0])    # By label/index
print(df.iloc[1])   # By integer position

# Data types
print(df.dtypes)

# Describe data
print(df.describe())

# Shape, columns, index
print(df.shape)
print(df.columns)
print(df.index)
```

---

## 🌐 5. Data Selection & Filtering

```python
# Condition-based filtering
print(df[df["Age"] > 25])

# Multiple conditions
print(df[(df["Age"] > 20) & (df["Age"] < 30)])

# isin()
print(df[df["Name"].isin(["Alice", "Charlie"])])
```

---

## 🧰 6. Data Cleaning

```python
# Check missing values
print(df.isnull())
print(df.isnull().sum())

# Drop missing
df.dropna()

# Fill missing
df.fillna(0)

# Rename columns
df.rename(columns={"Old": "New"})
```

---

## 📊 7. Aggregation & Grouping

```python
# Group by column
print(df.groupby("Age")["Name"].count())

# Aggregation
print(df["Age"].sum())
print(df["Age"].mean())
```

---

## 🌐 8. Working with CSV / Excel

```python
# Read CSV
pd.read_csv("data.csv")

# Save to CSV
df.to_csv("output.csv", index=False)

# Read Excel
pd.read_excel("data.xlsx")

# Save to Excel
df.to_excel("output.xlsx", index=False)
```

---

## 🚀 9. Advanced Functions

```python
# Apply function to column
print(df["Age"].apply(lambda x: x + 10))

# Sorting
print(df.sort_values(by="Age"))

# Drop column
df.drop("Age", axis=1)
```

---

## 🔗 10. Recommended Resources

### ✅ Official Documentation:

* [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

### ✅ W3Schools Pandas Tutorial:

* [https://www.w3schools.com/python/pandas/default.asp](https://www.w3schools.com/python/pandas/default.asp)

### ✅ TutorialsPoint Pandas:

* [https://www.tutorialspoint.com/python_pandas/index.htm](https://www.tutorialspoint.com/python_pandas/index.htm)

### ✅ YouTube (Bangla):

* "Anisul Islam Pandas"
* "Learn with Sumit"

---

## 🎯 11. Real-life Project Ideas

* COVID-19 data analysis
* Students grade sheet processing
* Sales & revenue dashboard
* Weather data visualization

---

## ✅ 12. Final Tips

* Practice daily using small CSV files
* Use Jupyter or VS Code
* Understand "indexing" properly
* Use `df.info()` and `df.describe()` often
* Don't memorize, just try it

---
