import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-15, 15, 500)
y = np.cos(x)/(1 + (1/5)*x**2)

plt.rc('mathtext', fontset = 'stix')


plt.figure()
plt.plot(x, y, 'C4')
plt.xlabel(r'$x$', fontsize = 14)
plt.ylabel(r'$y$', fontsize = 14)
plt.axvline(x = 0, color = 'gray', linestyle = '--', zorder = -1)
plt.axhline(color = 'gray', linestyle = '--', zorder = -1)
plt.tight_layout()
plt.show()