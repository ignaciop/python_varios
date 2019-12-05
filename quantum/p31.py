import numpy as np

x = float(input('x: '))

if x == -1:
    print('x = -1 not valid')
    x = float(input('x: '))
else:
    print(np.sin(x)/(1 + x))