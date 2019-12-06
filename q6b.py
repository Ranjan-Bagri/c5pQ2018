import matplotlib.pyplot as plt 
def f(t,x,v):
    return v
def g(t,x,v):
    return -w*x-b*v
t,x,v,h=0,1,0,0.01
w,b=1,1.0
T,V,A=[],[],[]
n=0
while n<=1000:
    a1=h*f(t,x,v)
    a2=h*f(t+h,x+a1,v+a1)
    b1=h*g(t,x,v)
    b2=h*g(t+h,x+b1,v+b1)
    x+=0.5*(a1+a2)
    v+=0.5*(b1+b2)
    t+=h
    T.append(t)
    V.append(x)
    A.append(v)
    n+=1
plt.plot(T,A,label='for $b=0.1,\omega_0=1$')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('Time(t)')
plt.ylabel('Position(x)')
plt.title('Motion of Damped Harmonic Oscillator')
plt.show()