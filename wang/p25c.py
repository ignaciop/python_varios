import numpy as np
import matplotlib.pyplot as plt
import ode

m = 1


def electron_ode(y, t):                  
    dydt = np.zeros(2)          
    dydt[0] = y[1]                
    dydt[1] = 1/(y[0]**2)                 
    
    return dydt 


def go():
    xrk2, vrk2 = 5, -1

    t, h = 0.0, 0.05
    tt = []
    
    xrk2_array, vrk2_array = [], []

    while t < 10:
        
        xrk2_array.append(xrk2)
        vrk2_array.append(vrk2)
        xrk2, vrk2 = ode.rk2(electron_ode, [xrk2, vrk2], t, h)

        tt.append(t)
        t += h


    plt.figure(1)
    plt.plot(tt, xrk2_array, '.', label = 'RK2')
    plt.xlabel('Time (s)')
    plt.ylabel('x (m)')
    plt.legend(loc = 'best')
    plt.show()
    
    plt.figure(2)
    plt.plot(tt, vrk2_array, '.', label = 'RK2')
    plt.xlabel('Time (s)')
    plt.ylabel('v (m/s)')
    plt.legend(loc = 'best')
    plt.show()

    plt.figure(3)
    plt.plot(xrk2_array, vrk2_array, '.', label = 'RK2')
    plt.xlabel('x (m)')
    plt.ylabel('v (m/s)')
    plt.legend(loc = 'best')
    plt.show()


go()
