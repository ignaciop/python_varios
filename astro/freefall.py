import numpy as np
import matplotlib.pyplot as plt

v0 = 0
y0 = 39969.4 # Altura desde donde se arroja Felix
rho = 0.004 # Tomo la densidad del aire a 39 km (punto del salto)
A = 0.4
m = 90
g = 9.81
c = 343

endtime = 40.0 # La prueba fue de 3.5 min; tomo 5 min (300 s)
steps = 100

t = np.linspace(0.0, endtime, steps)
dt = t[1]

v= np.zeros(len(t))
v[0] = v0

for i in range(0, steps - 1):
    v[i + 1] = v[i] + (g - (v[i]**2)*((rho*A)/(2*m)))*dt

   
y = y0 - v*t - 0.5*g*t**2
y = y[::-1]

vinv = v[::-1]

M = vinv/c

print('Terminal velocity (m/s): ', v[-1])

plt.figure()
plt.subplot(1,3,1)
plt.plot(t, v, 'r.-', markersize = 10, markeredgecolor = 'b')
plt.xlabel(r'time ($s$)')
plt.ylabel(r'velocity ($\frac{m}{s}$)')
plt.grid()
plt.axis('auto')

plt.subplot(1,3,2)
plt.plot(y, vinv, 'b.-', markersize = 10, markeredgecolor = 'r')
plt.ylabel(r'velocity ($\frac{m}{s}$)')
plt.xlabel(r'height ($m$)')
plt.xlim(y[-1],y[0])
plt.ylim(v[0],v[-1])
plt.grid()
plt.axis('auto')

plt.subplot(1,3,3)
plt.plot(y, M, 'y.-', markersize = 10, markeredgecolor = 'r')
plt.ylabel('Mach number')
plt.xlabel(r'height ($m$)')
plt.xlim(y[-1],y[0])
plt.ylim(M[-1],M[0])
plt.grid()
plt.axis('auto')
plt.show()

