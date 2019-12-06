import matplotlib.pyplot as plt 
def f(t,q):
    return -q/(C*R) 
R,C=1,1
t,q,h=0,500,0.01
T,Q=[],[]
n=0
while n<=1000:
    q+=h*f(t,q)
    t+=h
    T.append(t)
    Q.append(q)
    n+=1
plt.plot(T,Q,label='discharging curve')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('t')
plt.ylabel('q')
plt.title('Time variation of discharging of capacitor')
plt.show()