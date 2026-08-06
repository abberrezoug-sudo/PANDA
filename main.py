import pandas as pd
df = pd.read_csv("orders.csv")
print(df)
#PRINT THE FIRST 5 ROWS OF THE DATABASE
print(df.head())
#PRINT THE LAST 5 ROWS OF THE DATABASE
print(df.tail())
#General information about the database
print(df.info())
#General description
print(df.describe())
#get just the columns
print(df.columns)
#get index of the database
print(df.index)
#get by index
print(df["Country"])
print(df[["Country", "OrderID"]])
#par position
print(df.iloc[0])
print(df["Country"] == "USA")
#Updating DATA
df.loc[df["CustomerName"] == "Anna Ivanova", "Product"] = "New Product Name is time"
df = df.drop(39)