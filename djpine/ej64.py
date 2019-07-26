import numpy as np
import matplotlib.pyplot as plt

t, y, dy = np.loadtxt('ej64.txt', skiprows = 5, unpack = True)

t_t = np.linspace(0, 50, 100)
y_t = (3 + 0.5*np.sin(np.pi*t_t/5))*t_t*np.exp(-t_t/10)

fig, ax = plt.subplots()
ax.plot(t_t, y_t, 'b-', zorder = -1)
ax.errorbar(t, y, fmt = 'oC3', label = 'data', xerr = 0.75,
                yerr = dy, ecolor = 'black')
ax.set_xlabel('time (s)')
ax.set_ylabel('position (cm)')
plt.tight_layout()
plt.show()