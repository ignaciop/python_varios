import numpy as np
import matplotlib.pyplot as plt

def simpson(f, a, b, N):
    s_odd, s_even = 0.0, 0.0
    h = (b - a)/N
    
    for k in range(1, N, 2):
        s_odd += f(a + k*h)
        
    for k in range(2, N, 2):
        s_even += f(a + k*h)
        
    return (h/3)*(f(a) + f(b) + 4*s_odd + 2*s_even)
    

def E(x):
    return simpson(lambda t: np.exp(-t**2), 0, x, 1000)
    
xx = np.arange(0, 3, 0.1)
exx = [E(x) for x in xx]

plt.rc('text', usetex = True)
plt.rc('font', family = 'serif', size = 16)
plt.figure(figsize = (9, 7))
plt.plot(xx, exx, '.')
plt.xlabel('$x$')
plt.ylabel('$E(x)$')
plt.grid()
plt.show()