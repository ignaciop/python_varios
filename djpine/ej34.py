import numpy as np

g = 9.8
h0 = 10

y = np.arange(10, 0, -0.5)
t = np.sqrt(2*(h0 - y)/g)

print(y)
print(t)

deltat = t[1:] - t[:-1]
deltay = y[1:] - y[:-1]
v = deltay/deltat
print(v)

deltat2 = deltat[1:] - deltat[:-1]
deltav = v[1:] - v[:-1]
a = deltav/deltat2
print(a)