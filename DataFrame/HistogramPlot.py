import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = { 'values':[5,10,20,40,15,30,25],
         'age':[3,10,10,25,15,20,5],
         'marks':[30,15,30,20,30,40,55],
         'name':['a','b','c','d','e','f','g']}
df = pd.DataFrame(data)
ax=plt.gca()
df.plot(kind='line',x='name',y='values',ax=ax,color='green')
df.plot(kind='line',x='name',y='marks',ax=ax,color='r')
df.plot(kind='line',x='name',y='age',ax=ax,color='b')
plt.show()

df = pd.DataFrame(data)
plt.hist(df['values'],bins=5,edgecolor='red')
plt.show()
df.plot.density(color='green')
plt.show()

