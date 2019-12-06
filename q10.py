from math import pi,sqrt,sin
import matplotlib.pyplot as plt 
def f(t,theta,i):
    return i
def E(t):
    return 2*sin(w*t)
def g(t,theta,i):
    return (E(t)-R*i-theta/C)/L
R,L,C=0.02,1,0.25
w=sqrt(3.5)
t,theta,i=0,1,1
h=2*pi/60*w
n=0
while n<=1000:
    a1=h*f(t,theta,i)
    a2=h*f(t+h,theta+a1,i+a1)
    b1=h*g(t,theta,i)
    b2=h*g(t+h,theta+b1,i+b1)
    theta+=0.5*(a1+a2)
    i+=0.5*(b1+b2)
    t+=h
    n+=1
print(t,theta,i)