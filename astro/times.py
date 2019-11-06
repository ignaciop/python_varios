from math import sqrt

g = 9.81
v0 = float(input('Initial velocity: '))
y0 = float(input('Vertical position: '))

t1 = (v0 + sqrt(v0**2 - 2 * g * y0)) / g
t2 = (v0 - sqrt(v0**2 - 2 * g * y0)) / g

print('Time 1: {0:.2f} s\nTime 2: {1:.2f} s'.format(t1, t2))