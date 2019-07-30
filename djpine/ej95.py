import numpy as np
import matplotlib.pyplot as plt
from scipy.special import chebyt, hermitenorm

x = np.linspace(-1, 1, 100)
xx = np.linspace(-5, 5, 100)

t1 = np.polyval(chebyt(1), x)
t2 = np.polyval(chebyt(2), x)
t3 = np.polyval(chebyt(3), x)
t4 = np.polyval(chebyt(4), x)

h1 = np.polyval(hermitenorm(1), x)
h2 = np.polyval(hermitenorm(2), x)
h3 = np.polyval(hermitenorm(3), x)
h4 = np.polyval(hermitenorm(4), x)

plt.rc('mathtext', fontset = 'stix')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (9, 6))
ax1.plot(x, t1, label = r'$T_{1}(x)$')
ax1.plot(x, t2, label = r'$T_{2}(x)$')
ax1.plot(x, t3, label = r'$T_{3}(x)$')
ax1.plot(x, t4, label = r'$T_{4}(x)$')
ax1.legend(loc = 'best')
ax1.set_xlabel(r'$x$')
ax1.set_title('First four Chebyshev polynomials of the first kind')
ax1.grid()

ax2.plot(xx, h1, label = r'$H_{1}(x)$')
ax2.plot(xx, h2, label = r'$H_{2}(x)$')
ax2.plot(xx, h3, label = r'$H_{3}(x)$')
ax2.plot(xx, h4, label = r'$H_{4}(x)$')
ax2.legend(loc = 'best')
ax2.set_xlabel(r'$x$')
ax2.set_title('First four Hermite polynomials')
ax2.grid()

plt.tight_layout()
plt.show()

