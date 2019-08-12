import numpy as np

def I(N):
    y = []
    h = 2/N
    
    for k in range(N):
        xk = -1 + h*k
        yk = np.sqrt(1 - xk**2)
        y.append(yk)
        
    return h*sum(y)

real_value = np.pi/2

N = 100
i_value = I(N)

print('N = ',N)
print('Exact value: {0}\nComputed value: {1}\nDifference: {2}'
        .format(real_value, i_value, real_value - i_value))

N = 100000
i_value = I(N)

print('N = ',N)
print('Exact value: {0}\nComputed value: {1}\nDifference: {2}'
        .format(real_value, i_value, real_value - i_value))