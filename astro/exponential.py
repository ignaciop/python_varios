import numpy as np
import matplotlib.pyplot as plt

N0 = 100
tau = 5.0
endtime = 5.0
steps = 10

t = np.linspace(0.0, endtime, steps)
dt = t[1]

N = np.zeros(len(t))
N[0] = N0

answer = N0 * np.exp(-t/tau)

for i in range(steps - 1):
    N[i + 1] = N[i]*(1 - dt/tau)


plt.figure()
plt.plot(t, N, 'r.')
plt.plot(t, answer, zorder = -1)
plt.xlabel('Time')
plt.ylabel('Number of Nuclei')
plt.title('Comparison of analytical and numerical solutions')
plt.axis('auto')
plt.show()