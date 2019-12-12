import numpy as np

def perimeter(n):
    return 2*n*np.sin(np.pi/n)

def area_pol(n, a = 1):
    return 0.5*perimeter(n)*a

def area_unit_circle():
    return np.pi

values = [2**i for i in range(2,8)]

print('Unit Circle Area {0}: \n'.format(area_unit_circle()))

for j in values:
    a = area_pol(j)
    te = np.abs(area_pol(j) - area_unit_circle())
    print('N = {0} --> Polygon Area: {1} | Truncation {2}\n'.format(j, a, te))