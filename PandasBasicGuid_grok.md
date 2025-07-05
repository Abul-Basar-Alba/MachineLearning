# 📊 Complete Pandas Guide ( Resource Analysis)

---

## ✅ 1. Pandas Introduction

**Pandas** হলো Python-এর একটি শক্তিশালী এবং জনপ্রিয় লাইব্রেরি, যা ডেটা বিশ্লেষণ (data analysis), ডেটা ম্যানিপুলেশন (manipulation), এবং ডেটা ক্লিনিং (cleaning) এর জন্য ব্যবহৃত হয়। এটি বিশেষভাবে ডেটা সায়েন্টিস্ট, অ্যানালিস্ট এবং ডেভেলপারদের জন্য ডিজাইন করা হয়েছে। Pandas-এর মাধ্যমে আপনি সহজেই বড় ডেটাসেট নিয়ে কাজ করতে পারেন, যেমন CSV, Excel, SQL ডেটাবেস, বা JSON ফাইল।

### কেন Pandas ব্যবহার করবেন?
- **সহজ ডেটা হ্যান্ডলিং**: টেবুলার ডেটা (যেমন Excel বা SQL টেবিল) সহজে প্রসেস করা যায়।
- **দ্রুত এবং দক্ষ**: বড় ডেটাসেটেও দ্রুত কাজ করে।
- **বিস্তৃত ফাংশনালিটি**: ফিল্টারিং, গ্রুপিং, মার্জিং, এবং ডেটা ক্লিনিং-এর জন্য অনেক ফাংশন।
- **কমিউনিটি সাপোর্ট**: বড় কমিউনিটি এবং প্রচুর রিসোর্স।

### ইন্সটলেশন
Pandas ব্যবহার করতে প্রথমে এটি ইন্সটল করতে হবে:
```bash
pip install pandas
🔄 2. Key Pandas Data Structures
Pandas-এ দুটি প্রধান ডেটা স্ট্রাকচার রয়েছে: Series এবং DataFrame। এগুলো বোঝা খুবই গুরুত্বপূর্ণ কারণ এর ওপর ভিত্তি করে Pandas-এর সব কাজ হয়।

✅ Series
কী?: একটি 1D (এক মাত্রিক) অ্যারে, যা একটি কলামের মতো কাজ করে। এটি একটি ইনডেক্স (index) এবং ডেটা নিয়ে গঠিত।

উদাহরণ:
import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# Output:
# a    10
# b    20
# c    30
# dtype: int64
বৈশিষ্ট্য:
শুধু একটি কলামের ডেটা ধরে।
ইনডেক্স কাস্টমাইজ করা যায় (ডিফল্ট হলো 0, 1, 2...)।
ডেটা টাইপ (dtype) যেকোনো হতে পারে: int, float, string, ইত্যাদি।
✅ DataFrame
কী?: একটি 2D (দ্বি-মাত্রিক) টেবুলার ডেটা স্ট্রাকচার, যা একাধিক কলাম এবং রো নিয়ে গঠিত। এটি Excel স্প্রেডশিট বা SQL টেবিলের মতো।
উদাহরণ:

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Dhaka", "Chittagong", "Sylhet"]
})
print(df)
# Output:
#      Name  Age         City
# 0   Alice   25       Dhaka
# 1     Bob   30  Chittagong
# 2  Charlie   35      Sylhet
বৈশিষ্ট্য:
প্রতিটি কলাম একটি Series।
ইনডেক্স রো-এর জন্য, কলাম নাম কলামের জন্য।
যেকোনো ধরনের ডেটা (numeric, string, datetime) স্টোর করা যায়।

📃 3. Creating DataFrame (Different Ways)
DataFrame তৈরি করার জন্য বিভিন্ন উপায় রয়েছে। এখানে কিছু জনপ্রিয় পদ্ধতি:

1. Dictionary থেকে

data = {
    "Name": ["Rahim", "Karim", "Sadia"],
    "Age": [20, 25, 22],
    "City": ["Dhaka", "Rajshahi", "Khulna"]
}
df = pd.DataFrame(data)

2. List of Lists থেকে

data = [
    [1, "Rahim", "Dhaka"],
    [2, "Karim", "Chittagong"],
    [3, "Sadia", "Sylhet"]
]
df = pd.DataFrame(data, columns=["ID", "Name", "City"])

3. CSV/Excel থেকে

# CSV থেকে
df = pd.read_csv("data.csv")

# Excel থেকে
df = pd.read_excel("data.xlsx")

4. NumPy Array থেকে

import numpy as np
array = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(array, columns=["A", "B"])
টিপস:
CSV/Excel ফাইল ব্যবহার করার সময় ফাইলের পাথ সঠিক দিতে হবে।
ডেটার ধরন (dtype) নিয়ে সতর্ক থাকুন, যেমন সংখ্যা বা স্ট্রিং।

⚡ 4. Basic Operations
Pandas-এ ডেটা নিয়ে কাজ করার জন্য কিছু বেসিক অপারেশন জানা জরুরি। এগুলো দিয়ে ডেটা দেখা, অ্যাক্সেস করা, এবং বোঝা যায়।

✅ DataFrame দেখা

# প্রথম ৫টি রো
print(df.head())

# শেষ ৫টি রো
print(df.tail())

# নির্দিষ্ট সংখ্যক রো
print(df.head(3))  # প্রথম ৩টি রো
✅ কলাম অ্যাক্সেস

# একটি কলাম
print(df["Name"])  # Series হিসেবে ফিরে আসবে

# একাধিক কলাম
print(df[["Name", "City"]])  # DataFrame হিসেবে ফিরে আসবে
✅ রো অ্যাক্সেস
loc: ইনডেক্স লেবেল দিয়ে অ্যাক্সেস।

print(df.loc[0])  # প্রথম রো
print(df.loc[0:2])  # প্রথম থেকে তৃতীয় রো
iloc: ইনডেক্স পজিশন দিয়ে অ্যাক্সেস।

print(df.iloc[1])  # দ্বিতীয় রো
print(df.iloc[0:2])  # প্রথম দুটি রো
✅ ডেটা ইনফরমেশন
dtypes: প্রতিটি কলামের ডেটা টাইপ দেখায়।

print(df.dtypes)
# Output:
# Name    object
# Age      int64
# City    object
# dtype: object
describe(): সংখ্যাসূচক কলামের পরিসংখ্যান (মিন, ম্যাক্স, মিডিয়ান)।

print(df.describe())
shape: DataFrame-এর মাত্রা (রো, কলাম)।

print(df.shape)  # Output: (3, 3)
columns: কলামের নাম।

print(df.columns)  # Output: Index(['Name', 'Age', 'City'], dtype='object')
index: রো-এর ইনডেক্স।

print(df.index)  # Output: RangeIndex(start=0, stop=3, step=1)

🌐 5. Data Selection & Filtering
ডেটা ফিল্টারিং হলো Pandas-এর একটি শক্তিশালী ফিচার। এর মাধ্যমে আপনি নির্দিষ্ট শর্তের ভিত্তিতে ডেটা নির্বাচন করতে পারেন।

✅ Condition-based Filtering

# বয়স ২৫-এর বেশি
print(df[df["Age"] > 25])
# Output:
#      Name  Age         City
# 1     Bob   30  Chittagong
# 2  Charlie   35      Sylhet
✅ Multiple Conditions

# বয়স ২০-এর বেশি এবং ৩০-এর কম
print(df[(df["Age"] > 20) & (df["Age"] < 30)])
# Output:
#     Name  Age      City
# 0  Alice   25     Dhaka
✅ isin() Method

# নির্দিষ্ট নাম ফিল্টার
print(df[df["Name"].isin(["Alice", "Charlie"])])
# Output:
#      Name  Age    City
# 0   Alice   25   Dhaka
# 2  Charlie   35  Sylhet
✅ Query Method

# Query ব্যবহার করে ফিল্টার
print(df.query('Age > 25 and City == "Sylhet"'))
# Output:
#      Name  Age    City
# 2  Charlie   35  Sylhet
টিপস:
& (and), | (or), এবং ~ (not) ব্যবহার করুন শর্তের জন্য।
ফিল্টারিং-এর সময় ডেটা টাইপ ম্যাচ করতে হবে (যেমন, string বা int)।

🧰 6. Data Cleaning
ডেটা ক্লিনিং হলো Pandas-এর একটি গুরুত্বপূর্ণ অংশ। বাস্তব জগতের ডেটা প্রায়ই অসম্পূর্ণ বা ত্রুটিপূর্ণ হয়।

✅ Missing Values চেক করা

# কোন মান মিসিং কিনা চেক
print(df.isnull())
# মিসিং মানের সংখ্যা
print(df.isnull().sum())
✅ Missing Values হ্যান্ডলিং
Drop: মিসিং মান সম্বলিত রো বা কলাম মুছে ফেলা।

df.dropna()  # মিসিং মান সম্বলিত রো মুছে ফেলে
df.dropna(axis=1)  # মিসিং মান সম্বলিত কলাম মুছে ফেলে
Fill: মিসিং মান পূরণ করা।

df.fillna(0)  # মিসিং মান ০ দিয়ে পূরণ
df["Age"].fillna(df["Age"].mean())  # গড় দিয়ে পূরণ
✅ Rename Columns

# কলামের নাম পরিবর্তন
df.rename(columns={"Name": "Full_Name", "City": "Location"})
✅ ডুপ্লিকেট রিমুভ

# ডুপ্লিকেট রো মুছে ফেলা
df.drop_duplicates()
টিপস:
মিসিং ডেটা হ্যান্ডলিং-এর সময় ডেটার ধরন বিবেচনা করুন।
ডেটা ক্লিনিং-এর আগে ডেটা ব্যাকআপ করে নিন।

📊 7. Aggregation & Grouping
ডেটা গ্রুপিং এবং অ্যাগ্রিগেশন Pandas-এর শক্তিশালী ফিচার। এটি ডেটা সারাংশ করতে সাহায্য করে।

✅ Group By

# বয়সের ভিত্তিতে গ্রুপিং
print(df.groupby("City")["Age"].mean())
# Output:
# City
# Chittagong    30.0
# Dhaka         25.0
# Sylhet        35.0
# Name: Age, dtype: float64
✅ Aggregation
একাধিক অ্যাগ্রিগেশন ফাংশন ব্যব]}\

print(df.groupby("City").agg({"Age": ["mean", "min", "max"]}))
# Output:
#             Age
#            mean min max
# City
# Chittagong  30  30  30
# Dhaka       25  25  25
# Sylhet      35  35  35
✅ Common Aggregation Functions
sum(), mean(), median(), min(), max(), count(), std() (standard deviation)।
উদাহরণ:

print(df["Age"].sum())  # সব বয়সের যোগফল
print(df["Age"].mean())  # গড় বয়স

🌐 8. Working with CSV / Excel
Pandas CSV এবং Excel ফাইল নিয়ে কাজ করার জন্য খুবই উপযোগী।

✅ CSV
Read:

df = pd.read_csv("data.csv", encoding="utf-8")
encoding="utf-8" ব্যবহার করুন যদি ফাইলে বিশেষ ক্যারেক্টার থাকে।
Write:
df.to_csv("output.csv", index=False)  # ইনডেক্স ছাড়া সেভ

✅ Excel
Read:

df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
openpyxl বা xlrd লাইব্রেরি ইন্সটল করতে হবে:

bash
pip install openpyxl

Write:

df.to_excel("output.xlsx", index=False, sheet_name="Sheet1")
টিপস:
বড় ফাইলের জন্য chunksize প্যারামিটার ব্যবহার করুন।
ফাইল পড়ার সময় সঠিক sheet_name বা delimiter নিশ্চিত করুন।

🚀 9. Advanced Functions
Pandas-এর কিছু অ্যাডভান্সড ফাংশন ডেটা ম্যানিপুলেশনকে আরও শক্তিশালী করে।

✅ Apply Function

# প্রতিটি বয়সে ১০ যোগ করা
print(df["Age"].apply(lambda x: x + 10))
# Output:
# 0    35
# 1    40
# 2    45
# Name: Age, dtype: int64
✅ Sorting

# বয়সের ভিত্তিতে সর্ট
print(df.sort_values(by="Age", ascending=True))
# নাম এবং বয়সের ভিত্তিতে সর্ট
print(df.sort_values(by=["Name", "Age"]))
✅ Drop Column/Row

# কলাম মুছে ফেলা
df.drop("Age", axis=1)

# রো মুছে ফেলা
df.drop(0, axis=0)
✅ Merge/Join

df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Rahim", "Karim"]})
df2 = pd.DataFrame({"ID": [1, 2], "Score": [85, 90]})
merged_df = pd.merge(df1, df2, on="ID")
print(merged_df)
# Output:
#    ID   Name  Score
# 0   1  Rahim     85
# 1   2  Karim     90

🔗 10. Recommended Resources
✅ Official Documentation
লিঙ্ক: https://pandas.pydata.org/docs/
কেন উপযোগী?: Pandas-এর সমস্ত ফাংশন এবং মেথডের বিস্তারিত বর্ণনা। উদাহরণ এবং টিউটোরিয়াল রয়েছে।
✅ W3Schools Pandas Tutorial
লিঙ্ক: https://www.w3schools.com/python/pandas/default.asp
কেন উপযোগী?: সহজ এবং বেসিক টিউটোরিয়াল। নতুনদের জন্য আদর্শ।
✅ TutorialsPoint Pandas
লিঙ্ক: https://www.tutorialspoint.com/python_pandas/index.htm
কেন উপযোগী?: ধাপে ধাপে গাইড এবং প্রচুর উদাহরণ।
✅ YouTube (Bangla)
Anisul Islam: বাংলায় Pandas-এর বিস্তারিত টিউটোরিয়াল। বেসিক থেকে অ্যাডভান্সড টপিক কভার করে।
চ্যানেল: Anisul Islam
Learn with Sumit: ডেটা সায়েন্স এবং Pandas-এর বাংলা টিউটোরিয়াল। সহজ ভাষায় বোঝানো।
চ্যানেল: Learn with Sumit
✅ Additional Resources
Kaggle Pandas Tutorials: https://www.kaggle.com/learn/pandas
ইন্টারেক্টিভ টিউটোরিয়াল এবং প্র্যাকটিস প্রজেক্ট।
DataCamp: https://www.datacamp.com/courses/pandas-foundations
ফ্রি এবং পেইড কোর্স।

🎯 11. Real-life Project Ideas
নিচে কিছু বাস্তব জীবনের প্রজেক্ট আইডিয়া দেওয়া হলো যা দিয়ে আপনি Pandas শিখতে পারেন:

COVID-19 Data Analysis:
ডেটাসেট: Our World in Data
কাজ: কেস, মৃত্যু, এবং রিকভারির ডেটা বিশ্লেষণ। দেশভিত্তিক গ্রুপিং এবং ভিজুয়ালাইজেশন।
Pandas ফাংশন: groupby(), merge(), plot()।

Students Grade Sheet Processing:
ডেটাসেট: নিজের তৈরি CSV (নাম, বিষয়, নম্বর)।
কাজ: গড় নম্বর, পাস/ফেল স্ট্যাটাস, এবং টপ পারফর্মার নির্ণয়।
Pandas ফাংশন: apply(), sort_values(), describe()।

Sales & Revenue Dashboard:
ডেটাসেট: Kaggle-এর সেলস ডেটাসেট।
কাজ: মাসিক বিক্রি, প্রোডাক্ট ক্যাটাগরি অনুযায়ী রেভিনিউ, এবং ট্রেন্ড বিশ্লেষণ।
Pandas ফাংশন: pivot_table(), groupby(), plot()।

Weather Data Visualization:
ডেটাসেট: NOAA Weather Data
কাজ: তাপমাত্রা, বৃষ্টিপাতের ডেটা বিশ্লেষণ এবং গ্রাফ তৈরি।
Pandas ফাংশন: resample(), rolling(), plot()।

✅ 12. Final Tips
প্রতিদিন প্র্যাকটিস: ছোট ছোট CSV ফাইল নিয়ে কাজ করুন। Kaggle থেকে ডেটাসেট ডাউনলোড করুন।
Jupyter Notebook: ডেটা অ্যানালিসিসের জন্য Jupyter ব্যবহার করুন। এটি কোড এবং আউটপুট একসাথে দেখায়।
ইনডেক্সিং বোঝা: Pandas-এ ইনডেক্স খুবই গুরুত্বপূর্ণ। loc এবং iloc-এর পার্থক্য বুঝুন।
df.info() এবং df.describe(): ডেটাসেটের প্রাথমিক ধারণা পেতে এই ফাংশনগুলো ব্যবহার করুন।
মুখস্থ নয়, প্র্যাকটিস: ফাংশন মুখস্থ করার চেয়ে ছোট ছোট প্রজেক্টে ব্যবহার করুন।
কমিউনিটি থেকে শিখুন: Stack Overflow, Reddit, এবং Kaggle-এর ফোরামে প্রশ্ন করুন।


❤️ Always refer to official docs when in doubt. Practice is the key to mastering Pandas.


