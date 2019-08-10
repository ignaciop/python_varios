import numpy as np

g = 9.81
v0 = 0.0
h0 = float(input('Tower height (m): '))
h = 0

t1 = (v0 + np.sqrt(v0**2 - 2 * g * (h - h0))) / g

print('Ball hits the ground (h = {0:0.2f} meters) at {1:0.2f} seconds'
        .format(h, t1))