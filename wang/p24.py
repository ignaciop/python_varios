import numpy as np
import matplotlib.pyplot as plt
import ode

w = 1
m = 1

def oscillator(id, x, v, t):
    if (id == 0):
        return v
    else:
        return -x

def oscillator_rk(y, t):                  
    dydt = np.zeros(2)          
    dydt[0] = y[1]                
    dydt[1] = -w**2*y[0]                   
    
    return dydt 


def go():
    xlf, vlf = 1.5, 0.0
    xe, ve = 1.5, 0.0
    xrk2, vrk2 = 1.5, 0.0

    t, h = 0.0, 0.1
    tt = []
    xlf_array, vlf_array = [], []
    xe_array, ve_array = [], []
    xrk2_array, vrk2_array = [], []
    energy_lf, energy_e, energy_rk2 = [], [], []

    while t < 4*np.pi:
        xlf_array.append(xlf)
        vlf_array.append(vlf)
        energy_lf.append(0.5*m*vlf**2 + 0.5*m*w**2*xlf**2)
        xlf, vlf = ode.leapfrog(oscillator, xlf, vlf, t, h)

        xe_array.append(xe)
        ve_array.append(ve)
        energy_e.append(0.5*m*ve**2 + 0.5*m*w**2*xe**2)
        xe, ve = ode.Euler(oscillator_rk, [xe, ve], t, h)

        xrk2_array.append(xrk2)
        vrk2_array.append(vrk2)
        energy_rk2.append(0.5*m*vrk2**2 + 0.5*m*w**2*xrk2**2)
        xrk2, vrk2 = ode.rk2(oscillator_rk, [xrk2, vrk2], t, h)

        tt.append(t)
        t += h


    plt.figure(1)
    plt.plot(xlf_array, vlf_array, '--', label = 'Leapfrog')
    plt.plot(xe_array, ve_array,label = 'Euler')
    plt.plot(xrk2_array, vrk2_array, '.', label = 'RK2')
    plt.xlabel('x (m)')
    plt.ylabel('v (m/s)')
    plt.legend(loc = 'best')
    plt.show()

    plt.figure(2)
    plt.semilogy(tt, energy_lf, '--', label = 'Leapfrog')
    plt.semilogy(tt, energy_e, label = 'Euler')
    plt.semilogy(tt, energy_rk2, '.', label = 'RK2')
    plt.xlabel('Time (s)')
    plt.ylabel('Total Energy (J)')
    plt.legend(loc = 'best')
    plt.grid()
    plt.show()

go()
