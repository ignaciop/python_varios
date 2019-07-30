import numpy as np

eps = 10e-9

def trapezoid(f, a, b, N):
    x = np.linspace(a,b,N+1)
    y = f(x)
    y_right = y[1:] # Right endpoints
    y_left = y[:-1] # Left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    
    return T
    
f = lambda x: x**2
g = lambda x: np.sin(x)
h = lambda x: np.exp(-x**2)

qf = trapezoid(f, 2, 5, 5000)
qg = trapezoid(g, 0, np.pi, 5000)
qh = trapezoid(h, 0, 3.5, 5000)

print(qf, qg, qh)