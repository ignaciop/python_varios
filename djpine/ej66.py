import numpy as np
import matplotlib.pyplot as plt

t, p, u = np.loadtxt('ej66.txt', skiprows = 4, unpack = True)

deltat = t[1:] - t[-1:]
deltap = p[1:] - p[-1:]
duu = u / p
duuu = duu[1:] - duu[-1:]
v = deltap/deltat
uv = abs(v) * np.sqrt((duuu)**2)

deltat2 = deltat[1:] - deltat[-1:]
deltav = v[1:] - v[-1:]
a = deltav/deltat2
daa = uv / v
daaa = daa[1:] - daa[-1:]
ua = abs(a) * np.sqrt((daaa)**2)



fig, ax = plt.subplots(1, 3, sharex = True)
ax[1,1].errorbar(t, p, fmt = '.C4', label = 'position', 
                yerr = u, ecolor = 'black', barsabove = True)

ax[1,2].errorbar(deltat, v, fmt = '.C3', label = 'velocity',
                yerr = uv, ecolor = 'black', barsabove = True)

ax[1,3].errorbar(deltat2, a, fmt = '.C2', label = 'acceleration',
                yerr = daaa, ecolor = 'black', barsabove = True)
plt.tight_layout()
plt.show()