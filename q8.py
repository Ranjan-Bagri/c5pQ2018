import matplotlib.pyplot as plt 
from math import exp
def f(t,T):
    return -(T-65)/27
def g(t):
    return 65+(135*exp(-t))/27

t,T,h=0,200,1.0
time,temp,ex_temp=[],[],[]
n=0
while n<10:
    T+=h*f(t,T)
    t+=h
    time.append(t)
    temp.append(T)
    ex_temp.append(g(t))
    n+=h
print(time)
print(temp)
plt.plot(time,temp,label='solution by Euler method')
plt.plot(time,ex_temp,label='exact solution')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('t')
plt.ylabel('T')
plt.title('Numerical solution of given ODE')
plt.show()