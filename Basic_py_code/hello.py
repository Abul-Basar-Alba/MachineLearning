import pandas as pd

# data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
# df = pd.DataFrame(data)

# print(df)

df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A","B","C"],index=["x","y","z"])

# print(df.head(2))
# print(df.tail(2))
# print(df.index)
# print(df.columns)
# print(df.info)
print(df.describe())