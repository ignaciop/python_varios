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
    xrk4, vrk4 = 5, -4
    xrk45, vrk45 = 5, -4


    t, h = 0.0, 0.01
    tt = []
    
    xrk4_array, vrk4_array = [], []
    xrk45_array, vrk45_array = [], []


    while t < 4:
        
        xrk4_array.append(xrk4)
        vrk4_array.append(vrk4)
        xrk4, vrk4 = ode.rk4(electron_ode, [xrk4, vrk4], t, h)
        xrk45_array.append(xrk45)
        vrk45_array.append(vrk45)
        xrk45, vrk45 = ode.RK45n(electron_ode, [xrk45, vrk45], t, h)


        tt.append(t)
        t += h


    plt.figure(1)
    plt.plot(tt, xrk4_array, '.', label = 'RK4')
    plt.plot(tt, xrk45_array, '.', label = 'RK45')
    plt.xlabel('Time (s)')
    plt.ylabel('x (m)')
    plt.legend(loc = 'best')
    plt.show()
    
    plt.figure(2)
    plt.plot(tt, vrk4_array, '.', label = 'RK4')
    plt.plot(tt, vrk45_array, '.', label = 'RK45')
    plt.xlabel('Time (s)')
    plt.ylabel('v (m/s)')
    plt.legend(loc = 'best')
    plt.show()

    plt.figure(3)
    plt.plot(xrk4_array, vrk4_array, '.', label = 'RK4')
    plt.plot(xrk45_array, vrk45_array, '.', label = 'RK45')
    plt.xlabel('x (m)')
    plt.ylabel('v (m/s)')
    plt.legend(loc = 'best')
    plt.show()


go()
