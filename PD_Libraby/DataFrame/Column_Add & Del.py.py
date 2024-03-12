import pandas as pd

demo={'one':pd.Series([1,2,3,4],index=['a','b','c','d']),
      'two':pd.Series([1,2,3,4,5,6], index=['a','b','c','d','e','f'])}

df=pd.DataFrame(demo)
print("Created DataFrame..")
print(df)

print("Adding new column by passing series")
df['three']=pd.Series([23,34,44,55,],index=['a','b','c','d'])
print(df)

print("Add the existing column in dataframe")
df['four'] = df['one']+df['three']
df['five'] = df['two']+df['one']
print(df)

print("Deleting the colums using 'del' function")
del df['five']
del df['three']
print(df)

print("Delete a colum using 'pop' function")
df.pop('four')
print(df)



                                    
                        
