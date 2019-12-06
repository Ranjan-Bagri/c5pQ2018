import numpy as np
I=[5.12,7.80,9.26,10.90,11.70]
V=[2.1,3.2,3.8,4.5,4.8]
coeffs=np.polynomial.polynomial.polyfit(I,V,1) # V=IR
R=-(coeffs[1]/coeffs[0])
print("The value of R is %.3f kiloohm"%R)