import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

N = 10
x, w = gaussxw(N)


f = lambda x: x**4*np.exp(x)/(np.exp(x) - 1)**2

T = 5
tetaD = 428 #K
ro = 6.022e28 #m^-3
V = 1000
kb = 1.38e-23

def cv(T):
	
	a = 0
	b = tetaD/T 
	xp = 0.5*(b - a)*x + 0.5*(b + a)
	wp = 0.5*(b - a)*w
	
	s = sum(f(xp)*wp)

	return s

T = np.linspace(5, 500, 100)
C = [cv(Ti) for Ti in T]

plt.figure()
plt.plot(T,C)
plt.xlabel('Temperature, K')
plt.ylabel('$C_v$')
plt.show()