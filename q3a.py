import numpy as np 
import matplotlib.pyplot as plt 
theta=np.arange(0,2*np.pi,0.01)
a,b=2,5
x,y=a*np.cos(theta),b*np.sin(theta)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse')
plt.show()