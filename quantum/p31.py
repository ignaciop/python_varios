import numpy as np

x = float(input('x: '))

while x == -1:
    print('x = -1 not valid')
    x = float(input('x: '))

    
print(np.sin(x)/(1 + x)) 