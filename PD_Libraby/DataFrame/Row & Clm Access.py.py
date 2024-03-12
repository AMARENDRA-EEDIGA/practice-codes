import pandas as pd

info = { 'Name': pd.Series(["Amar","Anil","Venu","Kamal","Aman"], index=[1,2,3,4,5]),
         'Group': pd.Series(['MECs','MSCs','MPCs','MECs','BBA','BA'], index=[1,2,3,4,5,6])}

print(pd.DataFrame(info))
df=pd.DataFrame(info)

df['Year']=pd.Series(['1st','2nd','3rd','4th'],index=[1,2,3,4])
print(df)

# Select any column from the DataFrame using below code
print(df['Name'])



# Selecting a row by paaaing the row label and interger location to a 'loc' and 'iloc' functions respectively
print(df.loc[2])
print(df.iloc[0])

# In this DataFrame moule 'ROWS' starts from "zero to n-1"

# In this method we are using to select multiple rows by ':' operator.
print(df[2:4])


