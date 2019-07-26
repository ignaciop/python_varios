import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 3, 100)
y = 3*x**2

plt.figure()
plt.plot(x, y, 'C1')
plt.rc('mathtext', fontset = 'stix')
plt.xlabel(r'$x$', fontsize = 14)
plt.ylabel(r'$y$', fontsize = 14)
plt.show()