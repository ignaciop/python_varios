from math import factorial
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

def H(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    else:
        return 2*x*H(n - 1, x) - 2*n*H(n - 2, x)
        
def psi(n, x):
    return (1/np.sqrt(2**n*factorial(n)*np.sqrt(np.pi)))*np.exp(-x**2/2)*H(n, x)
        
x = np.linspace(-4, 4, 100)
psi0 = psi(0, x)*np.ones(len(x))
psi1 = psi(1, x)
psi2 = psi(2, x)
psi3 = psi(3, x)

plt.figure()        
plt.plot(x, psi0, label = '$\psi_0(x)$')
plt.plot(x, psi1, label = '$\psi_1(x)$')
plt.plot(x, psi2, label = '$\psi_2(x)$')
plt.plot(x, psi3, label = '$\psi_3(x)$')
plt.xlabel('$x$')
plt.legend(loc = 'best')
plt.tight_layout()
plt.grid()
plt.show()

x = np.linspace(-10, 10, 500)
psi30 = psi(30, x)


plt.figure()        
plt.plot(x, psi30, label = '$\psi_30(x)$')
plt.xlabel('$x$')
plt.legend(loc = 'best')
plt.tight_layout()
plt.grid()
plt.show()


#N = 50

#f = lambda x: (x**3)/(np.exp(x) - 1)

#x, w = gaussxw(N)

#def sigma_sb(u_):
	
#	a = 0
#	b = u_
#	xp = 0.5*(b - a)*x + 0.5*(b + a)
#	wp = 0.5*(b - a)*w
	
#	y = f(xp)
#	s = sum(y*wp)

#	return (kb**4/(4*np.pi**2*c**2*hbar**3))*s
	
#print('Stefan-Boltzmann constant (SI Units):', sigma_sb(710))
# Tomo u = 710 como infinito