import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 500)
sin = np.sin(x)
cos = np.cos(x)

plt.rc('mathtext', fontset = 'stix')


plt.figure()
plt.plot(x, sin, '-', color = 'orange', label = r'$sin (x)$')
plt.plot(x, cos, '-', color = 'green', label = r'$cos (x)$')
plt.xlabel(r'$x$', fontsize = 14)
plt.ylabel(r'$y$', fontsize = 14)
plt.legend(loc = 'best')
plt.axvline(x = 0, color = 'gray', linestyle = '--', zorder = -1)
plt.axhline(color = 'gray', linestyle = '--', zorder = -1)
plt.tight_layout()
plt.show()