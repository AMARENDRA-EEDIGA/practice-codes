import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sam_t_data = {'Data':['2020-01-25','2020-02-25','2020-03-25',
                     '2020-04-25','2020-05-25','2020-06-25',
                     '2020-07-25','2020-08-25','2020-09-25','2020-10-25'],
              'A':[232,535,643,435,634,453,643,634,233,532],
              'B':[1232,8535,3643,4435,6634,3453,3643,6343,2335,5323],
              'C':[23,45,23,77,32,78,23,98,23,76]
              }



df = pd.DataFrame(sam_t_data,columns=['Data','A','B','C'])

df = df.set_index('Data')
print(df)
plt.plot(df["A"])
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Sample time series plot")
plt.show()
df.plot(subplots=True, figsize=(12,15))
plt.show()
