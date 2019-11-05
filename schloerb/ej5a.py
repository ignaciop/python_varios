import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

t = np.linspace(0, 20, 21)
y = np.exp(t/10)*np.sin(t)
lf = interp1d(t, y)

tnew = np.arange(0, 20, 0.01)
ynew = lf(tnew)

plt.figure()
plt.plot(t, y, 'r.', label = 'Data')
plt.plot(tnew, ynew, '--', label = 'Spline interpolation' , zorder = -1)
plt.xlabel('t')
plt.ylabel('y')
plt.legend(loc = 'best')
plt.grid()
plt.show()