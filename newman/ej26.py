import numpy as np

M = 1.9891e30
G = 6.6738e-11


l1 = float(input('Perihelion (m): '))
v1 = float(input('Velocity at perihelion (m/s): '))

v2_roots = np.roots([1, -2*G*M/(v1*l1), -v1**2 + 2*G*M/l1])
v2 = np.min(v2_roots)

l2 = l1*v1/v2

a = 0.5*(l1 + l2)
b = np.sqrt(l1*l2)
T = 2*np.pi*a*b/(l1*v1)
e = (l2 - l1)/(l2 + l1)

print('Aphelion (m): ', l2)
print('Velocity at aphelion (m/s): ', v2)
print('Orbital period (s): ', T)
print('Orbital eccentricity: ', e)

