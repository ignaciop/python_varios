import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 100, 101)

A = float(input('What is the value of A: '))
B = float(input('What is the value of B: '))
C = float(input('What is the value of C: '))

cl = input('Plot color: ')
sy = input('Plot symbol: ')
st = input('Plot style: ')

y = A*t**3 + B*t**2 + C*t

plt.figure()
plt.plot(t, y, cl+sy+st)
plt.show()

