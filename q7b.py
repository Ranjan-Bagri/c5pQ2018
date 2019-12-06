import numpy as np 
import matplotlib.pyplot as plt 
def f(t,x,dxdt):
    return -k*x
t,x,dxdt=0,1,0
k=1
t_final,dt=25,0.01
T,V,A=[],[],[]
while t<=t_final:
    a1=dt*dxdt
    b1=dt*f(t,x,dxdt)
    a2=dt*(dxdt+0.5*b1)
    b2=dt*f(t+0.5*dt,x+0.5*a1,dxdt+0.5*b1)
    dx=0.5*(a1+a2)
    x+=dx
    dxdt+=0.5*(b1+b2)
    d2xdt2=dx/dt
    T.append(t)
    V.append(dxdt)
    A.append(d2xdt2)
    t+=dt
plt.plot(T,A,label='for k=1')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('Time(t)')
plt.ylabel('Position(x)')
plt.title('Motion of Simple Harmonic Oscillator(no friction)')
plt.show()