import numpy as np
import matplotlib.pyplot as plt
import ode

m = 1

def electron_ode_lf(id, x, v, t):
    if (id == 0):
        return v
    else:
        return 1/(x**2)


def go():
    xlf, vlf = 5, -1

    t, h = 0.0, 0.05
    tt = []
    
    xlf_array, vlf_array = [], []

    while t < 10:
        
        xlf_array.append(xlf)
        vlf_array.append(vlf)
        xlf, vlf = ode.leapfrog(electron_ode_lf, xlf, vlf, t, h)

        tt.append(t)
        t += h


    plt.figure(1)
    plt.plot(tt, xlf_array, '.', label = 'Leapfrog')
    plt.xlabel('Time (s)')
    plt.ylabel('x (m)')
    plt.legend(loc = 'best')
    plt.show()
    
    plt.figure(2)
    plt.plot(tt, vlf_array, '.', label = 'Leapfrog')
    plt.xlabel('Time (s)')
    plt.ylabel('v (m/s)')
    plt.legend(loc = 'best')
    plt.show()

    plt.figure(3)
    plt.plot(xlf_array, vlf_array, '.', label = 'Leapfrog')
    plt.xlabel('x (m)')
    plt.ylabel('v (m/s)')
    plt.legend(loc = 'best')
    plt.show()


go()
