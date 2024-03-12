import numpy as np
import pandas as pd

info = ({"C_1":[2334,54653,4345,np.nan,3463,3455,3463,3455],
         "C_2":[2334,54653,4345,65456,3463,3455,234,34],
         "C_3":[54653,np.nan,65456,3463,np.nan,234,34,53],
         "C_4":[54653,4345,65456,3463,3455,234,34,423],
         "C_5":[632,654,634,np.nan,4345,65456,3463,3455],
        "C_6":[54653,4345,65456,3463,3455,53,64,534]
        })

df = pd.DataFrame(info)
#print(df)


# It returns True if data is NaN, otherwise False
# print(df.isnull())

#It is quite opposite for isnull()
# print(df.notnull())

# Now we drop rows with at least one Nan value(Null value)
# print(df.dropna())
#print(df)

# Dropping columns with at least 1 null value.
#print(df.dropna(axis = 1))

#print(df.fillna(0))

# Filling null values with the previous ones
#print(df.fillna(method = 'pad'))

#print(df.fillna(method = 'bfill'))

#print(df.replace(np.nan,"amar"))

#print(df.interpolate(method = 'linear'))
#ValueError: time-weighted interpolation only works on Series or DataFrames with a DatetimeIndex
print(df.interpolate(method = 'time'))
#print(df.interpolate(method = 'quadratic'))
#print(df.interpolate(method = 'cubic'))
#print(df.interpolate(method = 'nearest'))
#print(df.interpolate(mentod = 'spline', order=2))
#print(df.interpolate(method = 'polynomial', order=2))
#print(df.interpolate(method = 'akima'))


      
                 
      






