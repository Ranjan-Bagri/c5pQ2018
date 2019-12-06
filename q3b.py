import matplotlib.pyplot as plt 
def f(t,q,i):
    return i
def g(t,q,i):
    return (E-q/C)/L
E,L,C=1,1,1
t,q,i=0,0,0
h=0.01
T,Q,I=[],[],[]
n=0
while n<=1000:
    a1=h*f(t,q,i)
    a2=h*f(t+h,q+a1,i+a1)
    b1=h*g(t,q,i)
    b2=h*g(t+h,q+b1,i+b1)
    q+=0.5*(a1+a2)
    i+=0.5*(b1+b2)
    t+=h
    T.append(t)
    Q.append(q)
    I.append(i)
    n+=1
plt.plot(T,I,label='current response curve')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('Time(t)')
plt.ylabel('Current(i)')
plt.title('Solution of differential equation  of LC circuit')
plt.show()