import numpy as np
import pandas as pd

##n = pd.DataFrame({'name':['a','b','c','d'],
##                 'age':[12,22,44,21],
##                 'markd':[53,44,66,32]},index=[10,20,30,40])
##
##print(n)
##print("Axes:m"+"\n",n.axes)
##print("Is Empty: "+"\n",n.empty)
##print("Ndim: "+"\n",n.ndim)
##print("Size: "+"\n",n.size)
##print("Actual Values: "+"\n",n.values)
##print("Each Column DataTypes: "+"\n",n.dtypes)
##print("Top 3 rows: "+"\n",n.head(3))
##print("Bottom 2 rows: "+"\n",n.tail(2))


n = pd.DataFrame({'name':[10.2,32,42.3,32],
                 'age':[12,22,44,21],
                 'markd':[53,44,66,32]},index=[10,20,30,40])

def custum_sum(row):
    return row.sum()

n['d']=n.apply(custum_sum,axis=1)
print(n)

n.loc[50]=n.apply(custum_sum,axis=0)
print(n)


