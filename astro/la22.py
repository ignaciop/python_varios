import numpy as np
import scipy.linalg as sp
import matplotlib.pyplot as plt

k = 15
m = 0.3

t = np.linspace(0, 10, 201)
M = np.array([[2, 0, -1, 0], [0, 2, 0, -1], [-1, 0, 1, 0], [0, -1, 0, 1]])

values, vectors = sp.eig(M)
rv = np.real(values)

eig1 = vectors[:,0]
eig2 = vectors[:,1]
eig3 = vectors[:,2]
eig4 = vectors[:,3]

w1 = np.sqrt(rv[0]/m)
w2 = np.sqrt(rv[1]/m)
w3 = np.sqrt(rv[2]/m)
w4 = np.sqrt(rv[3]/m)

x1 = eig1[0]*np.sin(w1*t) + eig1[1]*np.cos(w1*t)
x2 = eig2[0]*np.sin(w2*t) + eig2[1]*np.cos(w2*t)
x = x1 + x2

plt.figure()
plt.plot(t, x1, label = 'First mode')
plt.plot(t, x2, label = 'Second mode')
plt.plot(t, x, label = 'Original movement')
plt.xlabel('Time (s)')
plt.ylabel('x (m)')
plt.legend(loc = 'best')
plt.grid()
plt.show()