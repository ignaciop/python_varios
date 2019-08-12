import numpy as np
import matplotlib.pyplot as plt

m = np.loadtxt('stm.txt', float)

plt.figure()
plt.imshow(m)
plt.title('(111) Surface of Si')
plt.show()