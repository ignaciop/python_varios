import rootfinder as rtf
import numpy as np
import matplotlib.pyplot as plt


def go(v0):

    def f(R):
        return R*(vy + g/b)/vx + g*np.log(1 - b*R/vx)/(b**b)

    def df(R):
        return (vy + g/b)/vx - g/(b*(1 - b*R/vx)*vx)


    g, b = 9.8, 1.0
    x, yb, yn, dtr = [], [], [], np.pi/180

    for theta in range(1, 90):
        vx, vy = v0*np.cos(theta*dtr), v0*np.sin(theta*dtr)
        Rb = rtf.bisect(f, 0.01, vx/b - 1e-5, 1e-6)
        Rn = rtf.newton(f, df, vx/b - 1e-5)

        if (Rb != None and Rn != None):
            x.append(theta)
            yb.append(Rb)
            yn.append(Rn)

    plt.figure()
    plt.plot(x, yb, label = 'Bisection method', zorder = -1)
    plt.plot(x, yn, 'r.', label = 'Newton Method')
    plt.xlabel('angle (deg)')
    plt.ylabel('R (m)')
    plt.legend(loc = 'best')
    plt.title('v0 = {0}'.format(v0))
    plt.show()

for v0 in [10, 20, 50, 100, 200, 500]:
    go(v0)