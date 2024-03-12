import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\Swadha_MS-Office\SWADHA_MS_Office\MS-Excel/Data.csv")
df = pd.DataFrame(d)
df.info()
print("Statistical functions =", df.describe())
df['1801'].plot()
print("ploting")
plt.plot(subplots=True, figsize = (10,14))
plt.show()
