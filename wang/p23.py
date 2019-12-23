import numpy as np
import matplotlib.pyplot as plt
import ode

lamb = 0.5

def decay(y, t):                  
    dydt = np.zeros(1)          
    dydt[0] = -lamb*y[0]                                
                   
    return dydt            


t = 0
h = 0.5
y_euler, y_rk2, y_rk4, y_rk45n = 1000, 1000, 1000, 1000

tt, nuclear_euler, nuclear_rk2, nuclear_rk4, nuclear_rk45n = [], [], [], [], []

while t <= 8:
    yy_euler = ode.Euler(decay, [y_euler], t, h)
    yy_rk2 = ode.rk2(decay, [y_rk2], t, h)
    yy_rk4 = ode.rk4(decay, [y_rk4], t, h)
    yy_rk45n = ode.RK45n(decay, [y_rk45n], t, h)

    
    tt.append(t)
    nuclear_euler.append(yy_euler[0])
    nuclear_rk2.append(yy_rk2[0])
    nuclear_rk4.append(yy_rk4[0])
    nuclear_rk45n.append(yy_rk45n[0])

    y_euler = yy_euler[0]
    y_rk2 = yy_rk2[0]
    y_rk4 = yy_rk4[0]
    y_rk45n = yy_rk45n[0]

    t += h

plt.figure()
plt.plot(tt, nuclear_euler, label = 'Euler')
plt.plot(tt, nuclear_rk2, label = 'RK2')
plt.plot(tt, nuclear_rk4, label = 'RK4')
plt.plot(tt, nuclear_rk45n, label = 'RK45n')
plt.xlabel('Time (s)')
plt.ylabel('Nª of nuclei')
plt.grid()
plt.legend(loc = 'best')
plt.show()