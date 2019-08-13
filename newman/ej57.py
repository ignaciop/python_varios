import numpy as np

def f(x):
    return np.sin(np.sqrt(100*x))**2
    
def trapezoid(f, a, b, N):
    h = (b - a)/N
    s = 0.5*f(a) + 0.5*f(b)
    
    for k in range(1, N):
        s += f(a + k*h)
        
    return h*s
    
def adaptive_trapezoid(f, a, b, N, accuracy = 1e-6):
    Nn = N
    I1 = trapezoid(f, a, b, N)
    I2 = trapezoid(f, a, b, 2*N)
    e = (1/3)*(I2 - I1)
    
    while e > accuracy:
        Nn = 2*Nn
        I1 = I2
        I2 = trapezoid(f, a, b, Nn)
        e = (1/3)*(I2 - I1)
        
    return N, Nn, I2, e
    
    
real_value = 0.45
N, Nn, I, e = adaptive_trapezoid(f, 0, 1, 1)
N2, Nn2, I2, e2 = adaptive_trapezoid(f, 0, 1, 2)
N4, Nn4, I4, e4 = adaptive_trapezoid(f, 0, 1, 4)
N8, Nn8, I8, e8 = adaptive_trapezoid(f, 0, 1, 8)
N16, Nn16, I16, e16 = adaptive_trapezoid(f, 0, 1, 16)
N32, Nn32, I32, e32 = adaptive_trapezoid(f, 0, 1, 32)
N64, Nn64, I64, e64 = adaptive_trapezoid(f, 0, 1, 64)


print(Nn2)

print('Real value:', real_value)
print('Slices for N = {0}: {1}'.format(N, Nn))
print('Adaptive trapezoid rule value for N = {0}: {1}'.format(N, I))
print('Error for N = {0}: {1:0.32f}\n'.format(N, e))
print('Slices for N = {0}: {1}'.format(N2, Nn2))
print('Adaptive trapezoid rule value for N = {0}: {1}'.format(N2, I2))
print('Error for N = {0}: {1:0.32f}\n'.format(Nn2, e2))
print('Slices for N = {0}: {1}'.format(N4, Nn4))
print('Adaptive trapezoid rule value for N = {0}: {1}'.format(N4, I4))
print('Error for N = {0}: {1:0.32f}\n'.format(Nn4, e4))
print('Slices for N = {0}: {1}'.format(N8, Nn8))
print('Adaptive trapezoid rule value for N = {0}: {1}'.format(N8, I8))
print('Error for N = {0}: {1:0.32f}\n'.format(Nn8, e8))
print('Slices for N = {0}: {1}'.format(N16, Nn16))
print('Adaptive trapezoid rule value for N = {0}: {1}'.format(N16, I16))
print('Error for N = {0}: {1:0.32f}\n'.format(Nn16, e16))
print('Slices for N = {0}: {1}'.format(N32, Nn32))
print('Adaptive trapezoid rule value for N = {0}: {1}'.format(N32, I32))
print('Error for N = {0}: {1:0.32f}\n'.format(Nn32, e32))
print('Slices for N = {0}: {1}'.format(N64, Nn64))
print('Adaptive trapezoid rule value for N = {0}: {1}'.format(N64, I64))
print('Error for N = {0}: {1:0.32f}\n'.format(Nn64, e64))