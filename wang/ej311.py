import numpy as np
import matplotlib.pyplot as plt
import ode

def lin_drag(y, t):
    return np.array([y[2], y[3], -b1*y[2]/m, -g - b1*y[3]/m])

def go(vx = 5., vy = 5.):
    Y = [0., 0., vx, vy]
    t, h, x, y = 0., 0.01, [], []

    while Y[1] >= 0.0:
        x.append(Y[0])
        y.append(Y[1])

        Y = ode.rk4(lin_drag, Y, t, h)
        t += h

    plt.figure()
    plt.plot(x, y)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.grid()
    plt.show()

g, b1, m = 9.8, 1, 0.5
vx = 50*np.cos(np.deg2rad(20))
vy = 50*np.sin(np.deg2rad(20))
go(vx, vy)