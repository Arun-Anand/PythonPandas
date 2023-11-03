import pandas as pd
print ("arun")
df = pd.read_csv("C:\ARUNFILES\ALABS\PYPANDAS\MonthlyProductSales.csv", encoding = "ISO-8859-1")
print (df)
df.head()
print ("10 rows")
df.describe()
s = df["Product Name"]

s.value_counts(dropna=False)