import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

plt.figure(figsize = (9, 5))
plt.plot(x, y, label = 'Deltoid curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 'best')
plt.grid()
plt.show()

theta = np.linspace(0, 10*np.pi, 300)
r = theta**2

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.figure(figsize = (9, 5))
plt.plot(x, y, label = 'Galilean curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 'best')
plt.grid()
plt.show()

theta = np.linspace(0, 24*np.pi, 3000)
r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + np.sin(theta/12)**5

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.figure(figsize = (9, 5))
plt.plot(x, y, label = 'Fey\'s function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 'best')
plt.grid()
plt.show()