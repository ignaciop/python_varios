import numpy as np
import matplotlib.pyplot as plt

N0 = 100
tau = 5.0
endtime = 5.0
steps = 10
stepsize, error = [], []

answer  = N0 * np.exp(-endtime/tau)

for j in range(10):
    steps = steps * 2

    t = np.linspace(0.0, endtime, steps)
    dt = t[1]

    N = np.zeros(len(t))
    N[0] = N0
    N[1] = N[0]*(1 - dt/tau)

    for i in range(1,steps - 1):
        N[i + 1] = N[i - 1] - N[i]*2.0*dt/tau

    error.append((answer - N[steps-1]) / answer)
    stepsize.append(dt)

plt.figure()
plt.plot(stepsize, error, 'g.-', markersize = 10, markeredgecolor = 'k')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('step size')
plt.ylabel('relative error')
plt.title('Truncation Error in Euler Method')
plt.axis('auto')
plt.show()