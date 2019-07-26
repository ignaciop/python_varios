import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10000)
xx = np.random.randn(10000)

plt.figure()
plt.subplot(1,2,1)
plt.hist(x, bins = 50, histtype = 'bar', rwidth = 0.7, color = 'gray', label = 'np.random.rand(10000)')
plt.legend(loc = 'best')
plt.subplot(1,2,2)
plt.hist(xx, bins = 50, histtype = 'bar', rwidth = 0.7, color = 'gray', label = 'np.random.randn(10000)')
plt.legend(loc = 'best')
plt.show()