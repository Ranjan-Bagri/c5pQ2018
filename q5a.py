import numpy as np 
import matplotlib.pyplot as plt 
t=np.arange(-10,10,0.01)
a=2
x,y=a*t**2,2*a*t
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabola')
plt.show()