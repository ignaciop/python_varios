import numpy as np
from gaussxw import gaussxw

N = 50
kb = 8.31/6.02e23
c = 3e8
hbar = 6.63e-34/2/np.pi

f = lambda x: (x**3)/(np.exp(x) - 1)

x, w = gaussxw(N)

def sigma_sb(u_):
	
	a = 0
	b = u_
	xp = 0.5*(b - a)*x + 0.5*(b + a)
	wp = 0.5*(b - a)*w
	
	y = f(xp)
	s = sum(y*wp)

	return (kb**4/(4*np.pi**2*c**2*hbar**3))*s
	
print('Stefan-Boltzmann constant (SI Units):', sigma_sb(710))
# Tomo u = 710 como infinito