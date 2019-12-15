import numpy as np
import matplotlib.pyplot as plt

tl, pl, vl = [], [], []
h = 0.01
v = 0.0
p = 10
floor_height = 0.2
ball_radius = 1

for t in np.arange(0, 10, 0.5):
    tl.append(t)
    vl.append(v)

    p = p + v*h
    pl.append(p)

    if p > floor_height + ball_radius:
        v = v - 9.8*h
    else:
        v = -v

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(tl, pl, '-', label = 'Position')
plt.legend(loc = 'best')
plt.grid()
plt.subplot(1, 2, 2)
plt.plot(tl, vl, 'm-', label = 'Velocity')
plt.legend(loc = 'best')
plt.grid()
plt.show()