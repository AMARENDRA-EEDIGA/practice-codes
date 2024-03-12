import pandas as pd

d = pd.DataFrame([['Amar',20000],['Anil',30000]], columns = ['Ename','Salary'])

print(d)

d2= pd.DataFrame([['Kumar',50000],['Laadi',40000]], columns = ['Ename','Salary'])

d=pd.concat([d, d2], ignore_index=True)

# Add new rows to the DataFrame using 'cncat' method
print("Adding the rows from the existing DataFrame not using 'append()' function, but using 'concat' function")
print(d)

# Deletion of rows:
print("Delete the rows form the existing DataFrame using 'drop()' function")

print(d.drop(0))
                                                               

