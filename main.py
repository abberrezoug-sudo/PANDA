import pandas as pd
df = pd.read_csv("orders.csv")
print(df)
#PRINT THE FIRST 5 ROWS OF THE DATABASE
print(df.head())
#PRINT THE LAST 5 ROWS OF THE DATABASE
print(df.tail())
#generale information about the database
print(df.info())
#generale desccription
print(df.describe())
#get just the columns
print(df.columns)
#get index of the database
print(df.index)
#get by indexe
print(df["country"])
print(df[["country","order_id"]])
#par position
print(df.iloc[0])