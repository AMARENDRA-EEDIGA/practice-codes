import pandas as pd

d = pd.DataFrame([['Amar',60000],['Anil',30000],['Kumar'],['Amar',60000]], columns = ['Ename','Salary'])

print(d)

# Counts the each column items(in each coluns how many elements )
print(d.count())
# Counts by separating each row count individually 
print(d.count(axis='columns'))

# Note: We can sort DAtaFrames in different way as per our requeired like by index(ascending=False or axis),lable,by actual value
# Sorting based on the actual values of the column
print(d.sort_values(by='Salary'))

print(d.drop_duplicates())
                    
