import numpy as np
import matplotlib.pyplot as plt

N0 = 100
endtime = 25
steps20 = 20
steps40 = 40
steps80 = 80

tau = float(input('Mean lifetime: '))
t20 = np.linspace(0.0, endtime, steps20)
t40 = np.linspace(0.0, endtime, steps40)
t80 = np.linspace(0.0, endtime, steps80)
dt20 = t20[1]
dt40 = t40[1]
dt80 = t80[1]

N20 = np.zeros(len(t20))
N20[0] = N0
N40 = np.zeros(len(t40))
N40[0] = N0
N80 = np.zeros(len(t80))
N80[0] = N0

answer = N0 * np.exp(-t20/tau)

for i in range(steps20 - 1):
    N20[i + 1] = N20[i]*(1 - dt20/tau)

for i in range(steps40 - 1):
    N40[i + 1] = N40[i]*(1 - dt40/tau)

for i in range(steps80 - 1):
    N80[i + 1] = N80[i]*(1 - dt80/tau)


plt.figure()
plt.plot(t20, N20, 'b.', label = '20')
plt.plot(t40, N40, 'g.', label = '40')
plt.plot(t80, N80, 'r.', label = '80')
plt.plot(t20, answer, zorder = -1, label = 'analytical')
plt.xlabel('Time')
plt.ylabel('Number of Nuclei')
plt.title('Comparison of analytical and numerical solutions')
plt.axis('auto')
plt.legend(loc = 'best')
plt.show()