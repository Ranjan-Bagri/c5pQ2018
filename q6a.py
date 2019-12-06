import numpy as np 
a=np.array([[3,2,4],[2,1,1],[1,3,5]])
b=np.array([7,4,2])
I=np.linalg.solve(a,b)
print('X1=%.3f'%I[0])
print('X2=%.3f'%I[1])
print('x3=%.3f'%I[2])