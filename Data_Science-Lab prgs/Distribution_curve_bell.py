import numpy as np
import matplotlib.pyplot as plt
import seaborn

def pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std*np.sqrt(2*np.pi))*np.exp(-(x-mean)**2/(2*std**2))
    return y_out

x = np.arange(-2,2,0.1)
y=pdf(x)
#plt.style.use('seaborn')
plt.plot(x,y,color='b',linestyle='dashed')
plt.scatter(x,y,marker='o', s=5, color='red')
plt.show()



