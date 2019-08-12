import numpy as np
import matplotlib.pyplot as plt

month, sunspots = np.loadtxt('sunspots.txt', unpack = True)
r = 5
Y = []

for k in range(len(sunspots)):
    Yk = (1/(2*r))*sum(sunspots[k - r:k + r])
    Y.append(Yk)

plt.figure(figsize = (9, 5))
plt.plot(month, sunspots, '.', label = 'Data')
plt.plot(month[:1000], sunspots[:1000], '.', label = 'First 1000 points')
plt.plot(month[:1000], Y[:1000], '-', label = 'Running average')
plt.xlabel('Month')
plt.ylabel('Sunspots')
plt.legend(loc = 'best')
plt.show()