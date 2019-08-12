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
    
def J(m, x):
    return (1/np.pi)*simpson(lambda theta: np.cos(m*theta - x*np.sin(theta)), 0, np.pi, 1000)

    
x = np.arange(0, 20, 0.1)
j0 = J(0, x)
j1 = J(1, x)
j2 = J(2, x)

plt.rc('text', usetex = True)
plt.rc('font', family = 'serif', size = 14)
plt.figure(figsize = (9, 7))
plt.plot(x, j0, '-', label = '$J_0(x)$')
plt.plot(x, j1, '-', label = '$J_1(x)$')
plt.plot(x, j2, '-', label = '$J_2(x)$')
plt.xlabel('$x$')
plt.xlim([0., 20.])
plt.legend(loc = 'best')
plt.grid()
plt.show()

l = 500
k = 2*np.pi/l
x = np.arange(-200, 200) # mas de 200 tarda mucho...
y = np.arange(-200, 200)
X, Y = np.meshgrid(x, y)

r = np.sqrt(X**2 + Y**2)
I = (J(1, k*r)/(k*r))**2

plt.figure(figsize = (9, 7))
plt.imshow(I, cmap = plt.cm.hot)
plt.title('Diffraction pattern of a point light source with $\lambda$ = {0} nm'
            .format(l))
plt.grid()
plt.show()