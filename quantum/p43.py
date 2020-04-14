import numpy as np

x0 = 1
x1 = 2
tol = 1e-15

def f(x):
    return np.sqrt(x + 1)*np.cos(x/2)**3

for i in range(500):
    fx0 = f(x0)
    fx1 = f(x1)

    x2 = x1 - fx1*(x1 - x0)/(fx1 - fx0)

    interval = abs(x2 - x1)/abs(x1)

    if interval <= tol:
        N = i + 1
        rootFound = True
        break

    x0 = x1
    x1 = x2
    
else:
    rootFound = False

if rootFound:
    print('After {} iterations, the root is {}'.format(N, x2))
else:
    print('Secant method did not converge')
