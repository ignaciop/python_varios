import numpy as np
import matplotlib.pyplot as plt
import ode

lamb = 0.5

def decay(y, t):                  
    dydt = np.zeros(1)          
    dydt[0] = -lamb*y[0]                                
                   
    return dydt            

def exact_sol(t):
    return 1000*np.exp(-lamb*t)

t = 0
h = 0.5
y_euler, y_rk2, y_rk4, y_rk45n = 1000, 1000, 1000, 1000

tt, exsol = [], []
nuclear_euler, nuclear_rk2, nuclear_rk4, nuclear_rk45n = [], [], [], []
abserr_euler, abserr_rk2, abserr_rk4, abserr_rk45n = [], [], [], []
clf_euler, clf_rk2, clf_rk4, clf_rk45n = [], [], [], []

while t <= 8:
    yy_euler = ode.Euler(decay, [y_euler], t, h)
    yy_rk2 = ode.rk2(decay, [y_rk2], t, h)
    yy_rk4 = ode.rk4(decay, [y_rk4], t, h)
    yy_rk45n = ode.RK45n(decay, [y_rk45n], t, h)

    exs = exact_sol(t)
    
    tt.append(t)
    exsol.append(exs)

    nuclear_euler.append(yy_euler[0])
    nuclear_rk2.append(yy_rk2[0])
    nuclear_rk4.append(yy_rk4[0])
    nuclear_rk45n.append(yy_rk45n[0])
    abserr_euler.append(abs(yy_euler[0] - exs))
    abserr_rk2.append(abs(yy_rk2[0] - exs))
    abserr_rk4.append(abs(yy_rk4[0] - exs))
    abserr_rk45n.append(abs(yy_rk45n[0] - exs))
    clf_euler.append(t*(1000 - yy_euler[0]))
    clf_rk2.append(t*(1000 - yy_rk2[0]))
    clf_rk4.append(t*(1000 - yy_rk4[0]))
    clf_rk45n.append(t*(1000 - yy_rk45n[0]))


    y_euler = yy_euler[0]
    y_rk2 = yy_rk2[0]
    y_rk4 = yy_rk4[0]
    y_rk45n = yy_rk45n[0]

    t += h

print('Lifetime tau (Euler): ', np.average(clf_euler))
print('Lifetime tau (RK2): ', np.average(clf_rk2))
print('Lifetime tau (RK4): ', np.average(clf_rk4))
print('Lifetime tau (RK45n): ', np.average(clf_rk45n))


plt.figure(1)
plt.plot(tt, exsol, '--', label = 'Exact solution $N(t) = 1000e^{-\lambda t}, \lambda = 0.5 min^{-1}$', zorder = 1)
plt.plot(tt, nuclear_euler, label = 'Euler')
plt.plot(tt, nuclear_rk2, label = 'RK2')
plt.plot(tt, nuclear_rk4, label = 'RK4')
plt.plot(tt, nuclear_rk45n, label = 'RK45n')
plt.xlabel('Time (s)')
plt.ylabel('Nº of nuclei')
plt.grid()
plt.legend(loc = 'best')
plt.show()

plt.figure(2)
plt.semilogy(tt, abserr_euler, label = 'Euler')
plt.semilogy(tt, abserr_rk2, label = 'RK2')
plt.semilogy(tt, abserr_rk4, label = 'RK4')
plt.semilogy(tt, abserr_rk45n, label = 'RK45n')
plt.xlabel('Time (s)')
plt.ylabel('Absolute error')
plt.grid()
plt.legend(loc = 'best')
plt.show()