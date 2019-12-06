def f(t,theta):
    return K*(100-theta)
theta,K,n,h=90,2.5,0,0.01
t,t_final=0,2.0
while n<=t_final:
    k1=h*f(t,theta)
    k2=h*f(t+h,theta+k1)
    theta+=0.5*(k1+k2)
    t+=h
    n+=0.01
print('The value of q at t=2.0 sec is %.3f unit'%(theta/t))