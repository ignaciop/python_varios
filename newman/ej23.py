import numpy as np

x = float(input('x: '))
y = float(input('y: '))

r = np.sqrt(x**2 + y**2)
theta = np.degrees(np.arctan2(y, x))

print('Module: {0:0.2f}, Degrees: {1:0.1f}'.format(r, theta))