import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 100, 101)
y = 4*t**3 - 3*t**2 + 7*t

plt.figure()
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('y = 4*t**3 - 3*t**2 + 7*t')
plt.grid()
plt.show()

