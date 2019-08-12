import numpy as np
import matplotlib.pyplot as plt

e = 1.602e-19

freq, volts = np.loadtxt('millikan.txt', unpack = True)

N = len(freq)
Ex = (1/N)*sum(freq)
Ey = (1/N)*sum(volts)
Exx = (1/N)*sum(freq**2)
Exy = (1/N)*sum(freq*volts)

m = (Exy - Ex*Ey)/(Exx - Ex**2)
c = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)

V = m*freq + c

# Si tengo m, de la ecuacion de V = h/e*nu + phi = m*freq + c; sale h = me
h = m*e
print(h)

plt.figure()
plt.plot(freq, volts, '.', label = 'Data')
plt.plot(freq, V, '-', label = 'Fitted line', zorder = -1)
plt.xlabel('Frecuency (Hz)')
plt.ylabel('Volts (V)')
plt.legend(loc = 'best')
plt.show()