import numpy as np
import matplotlib.pyplot as plt
from dtrig import cosd, sind

x, y = [], []

for g in range(0, 361):
    x.append(cosd(g))
    y.append(sind(g))

plt.figure()
plt.plot(x, y)
plt.grid()
plt.show()