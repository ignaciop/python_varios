import numpy as np

c = 1

x = float(input('Position of the planet (light years): '))
v = float(input('Velocity (0 < v < c = 1): ' ))

beta = np.sqrt(1 - (v**2 / c**2))
t_ship = x / v
t_earth = t_ship / beta

print('From ship frame of reference: {0:0.2f} years\nFrom Earth\'s frame of reference: {1:0.2f} years'.
        format(t_ship, t_earth))