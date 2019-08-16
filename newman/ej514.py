from math import factorial
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

G = 6.674e-11
m = 1
ro = 100
f = lambda x,y,z: (x**2 + y**2 + z**2)**-3/2

N = 100
x,w = gaussxw(N)

def force(z):
	
	a = -5
	b = 5
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	yp = xp
	
	wp = 0.5*(b-a)*w
	
	s=0
	for i in range(N):
		for j in range(N):
			s+=wp[i]*wp[j]*f(xp[i],yp[j],z)
		
	F  = G * m * ro * z *s
	return F

z = np.linspace(0,10,50)
F = [force(zi) for zi in z]

plt.figure()
plt.plot(z,F)
plt.xlabel('z, m')
plt.ylabel('Force, N')
plt.grid()
plt.show()