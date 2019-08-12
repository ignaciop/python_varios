import numpy as np
import matplotlib.pyplot as plt

    
def trapezoidal(t, v):
    a = t[0]; b = t[-1];
    N = len(t); # this is the number of intervals

    h = (b - a)/N; # this is the width of each interval

    s = 0.0
    ss = []
    ss.append(s)
    for k in range(len(t) - 1):
        s += 0.5 * ((t[k+1] - t[k]) * (v[k+1] + v[k]))
        ss.append(s)
        
    return h*s, ss

t, v = np.loadtxt('velocities.txt', unpack = True)

f, ss = trapezoidal(t, v)
print('Distance traveled (m): ',f)

plt.figure()
plt.plot(t, v, '.', label = 'Data')
plt.plot(t, ss, '.', label = 'Integration')
plt.legend(loc = 'best')
plt.show()