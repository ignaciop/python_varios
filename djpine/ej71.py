import numpy as np
import matplotlib.pyplot as plt

def besseln(x, n):
    if n == 0:
        return np.sin(x)/x
    elif n == 1:
        return np.sin(x)/x**2 - np.cos(x)/x
    elif n == 2:
        return (3/x**2 - 1)*(np.sin(x)/x) - 3*np.cos(x)/x**2
        
a = np.linspace(0, 20, 250)
j0 = besseln(a, 0)
j1 = besseln(a, 1)
j2 = besseln(a, 2)

plt.figure()
plt.rc('mathtext', fontset = 'stix')
plt.plot(a, j0, 'C1-', label = r'$j_{0}(x)$')
plt.plot(a, j1, 'C2--', label = r'$j_{1}(x)$')
plt.plot(a, j2, 'C3-', label = r'$j_{2}(x)$')
plt.legend(loc = 'best')
plt.xlabel(r'$x$')
plt.axhline(color = 'gray', linestyle = '-', zorder = -1)
plt.tight_layout()
plt.show()