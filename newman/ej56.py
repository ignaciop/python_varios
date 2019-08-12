import numpy as np

def f(x):
    return x**4 - 2*x + 1
    
def trapezoid(f, a, b, N):
    h = (b - a)/N
    s = 0.5*f(a) + 0.5*f(b)
    
    for k in range(1, N):
        s += f(a + k*h)
        
    return h*s
    
real_value = 4.4
I1 = trapezoid(f, 0, 2, 10)
I2 = trapezoid(f, 0, 2, 20)
e2 = (1/3)*(I2 - I1)

print('Real value:', real_value)
print('Trapezoid rule value for N = 10: {0}'.format(I1))
print('Trapezoid rule value for N = 20: {0}\n'.format(I2))
print('Error e2:', e2)
print('Direct computation of error for N = 10:', real_value - I1)
print('Direct computation of error for N = 20:', real_value - I2)