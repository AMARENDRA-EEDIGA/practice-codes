import numpy as np
import pandas as pd

n = pd.DataFrame({'name':[10.2,32,42.3,32],
                 'age':[12,22,44,21],
                 'markd':[53,44,66,32]},index=[10,20,30,40])



##def custum_sum(row):
##    return row.sum()


##n['d']=n.apply(custum_sum,axis=1)
##print(n)
##
##n.loc[50]=n.apply(custum_sum,axis=0)
##print(n)

def custum_mul(row):
    return row*2
##
##n['e']=n['markd'].apply(custum_mul)
##print(n)

##
##n['f'] = n.apply(lambda x:x.sum(),axis=1)
##n.loc[50] = n.apply(lambda x:x.sum(), axis=0)
##n.loc[60] = n.loc[10].apply(lambda x:x*2)
##print(n)

print(n)
print(n.map(np.square))
result_df = n.map(lambda row:custum_mul(row))
print(result_df)
print(n.map(lambda row:row**2))




