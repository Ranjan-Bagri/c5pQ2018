import matplotlib.pyplot as plt 
def f(t,q):
    return (E-q/C)/R 
R,C,E=1,1,1
t,q,h=0,0,0.01
T,Q=[],[]
n=0
while n<=1000:
    q+=h*f(t,q)
    t+=h
    T.append(t)
    Q.append(q)
    n+=1
plt.plot(T,Q,label='charging curve')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('t')
plt.ylabel('q')
plt.title('Time variation of charging of capacitor')
plt.show()