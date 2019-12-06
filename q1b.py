import matplotlib.pyplot as plt 
def f(x,y):
    return -lmbda*y
x,y,h=0,100,0.01
lmbda=1.50
X,Y=[],[]
n=0
while n<=1000:
    y+=h*f(x,y)
    x+=h
    X.append(x)
    Y.append(y)
    n+=1
plt.plot(X,Y,label='radioactive decay curve')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of radioactive decay equation')
plt.show()