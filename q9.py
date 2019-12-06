import numpy as np 
import matplotlib.pyplot as plt
m=np.array([50,100,150,200,250])
x=np.array([2,4,6,8,11])
coeffs=np.polynomial.polynomial.polyfit(m,x,1)
y=coeffs[1]*m+coeffs[0]
plt.scatter(m,x,label='data points')
plt.plot(m,y,label='best fitted line')
plt.xlabel('mass')
plt.ylabel('displacement')
plt.title("Experimental verification of Hooke's law")
plt.show()