import numpy as np

t = np.arange(0, 11, 2)

A = float(input('What is the value of A: '))
B = float(input('What is the value of B: '))
C = float(input('What is the value of C: '))

y = A*t**3 + B*t**2 + C*t
print(y)

for tt in t:
    y2 = A*tt**3 + B*tt**2 + C*tt
    print('t = ', tt, 'y = ', y2)

