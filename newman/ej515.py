import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 + 0.5*np.tanh(2*x)
    
h = 0.5

x = np.linspace(-2, 2, 100)
diff = (f(x + h/2) - f(x - h/2))/h
diff_a = -np.tanh(2*x)**2 + 1

plt.figure()
plt.plot(x, diff, label = 'Numerical')
plt.plot(x, diff_a, label = 'Analytical')
plt.xlabel('x')
plt.legend(loc = 'best')
plt.grid()
plt.show()
