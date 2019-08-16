from math import factorial
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

def H(n, x):
    i = 2
    H0 = 1
    H1 = 2*x
    H = 0
    
    if n == 0:
        H = H0
    elif n == 1:
        H = H1
    else:
        while i <= n:
            H = 2*x*H1 - 2*n*H0
            H0 = H1
            H1 = H
            i += 1
        
    return H
        
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
plt.plot(x, psi30, label = '$\psi_{30}(x)$')
plt.xlabel('$x$')
plt.legend(loc = 'best')
plt.tight_layout()
plt.grid()
plt.show()


N = 100

f = lambda x: x**2*np.abs(psi(5, x))**2

x, w = gaussxw(N)

def rms2(u_):
	
	a = -u_
	b = u_
	xp = 0.5*(b - a)*x + 0.5*(b + a)
	wp = 0.5*(b - a)*w
	
	y = f(xp)
	s = sum(y*wp)

	return np.sqrt(s)
	
print('Uncertainty of a particle on the 5th level:', rms2(1.1))