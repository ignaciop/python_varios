import numpy as np
import matplotlib.pyplot as plt

def gamma(a, x):
    return np.exp((a - 1)*np.log(x))*np.exp(-x)
    
x = np.linspace(0, 5, 100)
g2 = gamma(2, x)
g3 = gamma(3, x)
g4 = gamma(4, x)

plt.figure()
plt.plot(x, g2, label = '$\Gamma(2)$')
plt.plot(x, g3, label = '$\Gamma(3)$')
plt.plot(x, g4, label = '$\Gamma(4)$')
plt.xlabel('$x$')
plt.legend(loc = 'best')
plt.grid()
plt.show()
