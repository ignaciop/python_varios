import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(yy, t, params):
    x, y, z = yy
    a, b, c = params
    derivs = [a*(y - x), (c - a)*x - x*z + c*y, x*y - b*z]
    
    return derivs

# Parametros caoticos
a = 40
#b = 5
c = 35

# Parametros periodicos
b = 10

# Valores iniciales
x0 = -10
y0 = 0
z0 = 35

params = [a, b, c]
yy0 = [x0, y0, z0]

tStop = 10.
tInc = 0.05
t = np.arange(0., tStop, tInc)

psoln = odeint(f, yy0, t, args = (params,))

plt.rc('mathtext', fontset = 'stix')
fig = plt.figure(figsize = (9.5, 6.5))

ax1 = fig.add_subplot(321)
ax1.plot(t, psoln[:,0], color = 'black')
ax1.set_xlabel('time')
ax1.set_ylabel(r'$x$', fontsize = 14)

ax2 = fig.add_subplot(323)
ax2.plot(t, psoln[:,1], color = 'black')
ax2.set_xlabel('time', fontsize = 14)
ax2.set_ylabel(r'$y$', fontsize = 14)

ax3 = fig.add_subplot(325)
ax3.plot(t, psoln[:,2], color = 'black')
ax3.set_xlabel('time', fontsize = 14)
ax3.set_ylabel(r'$z$', fontsize = 14)


ax4 = fig.add_subplot(322)
ax4.plot(psoln[:,0], psoln[:,1], dashes = (1,2), ms = 1, color = 'C1')
ax4.set_xlabel(r'$x$', fontsize = 14)
ax4.set_ylabel(r'$y$', fontsize = 14)

ax5 = fig.add_subplot(324)
ax5.plot(psoln[:,2], psoln[:,1], dashes = (1,2), ms = 1, color = 'C2')
ax5.set_xlabel(r'$z$', fontsize = 14)
ax5.set_ylabel(r'$y$', fontsize = 14)

ax6 = fig.add_subplot(326)
ax6.plot(psoln[:,0], psoln[:,2], dashes = (1,2), ms = 1, color = 'C4')
ax6.set_xlabel(r'$x$', fontsize = 14)
ax6.set_ylabel(r'$z$', fontsize = 14)

plt.tight_layout()
plt.show()