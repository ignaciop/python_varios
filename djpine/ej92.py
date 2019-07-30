import numpy as np
from scipy.integrate import quad

f = lambda x: 1/(1 + x**2)
g = lambda x: 1/((np.exp(x) + x + 1)**2 + np.pi**2)
qf = quad(f, -1, 1)
qg = quad(g, -np.inf, np.inf)
print(qf[0])
print(qg[0])