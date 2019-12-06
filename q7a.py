import numpy as np 
a=np.array([[50,0,-30],[0,40,-20],[-30,-20,100]])
b=np.array([80,80,0])
I=np.linalg.solve(a,b)
print('I1=%.3f'%I[0])
print('I2=%.3f'%I[1])
print('I3=%.3f'%I[2])