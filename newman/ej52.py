import numpy as np

def f(x):
    return x**4 - 2*x + 1
    
def simpson(f, a, b, N):
    s_odd, s_even = 0.0, 0.0
    h = (b - a)/N
    
    for k in range(1, N, 2):
        s_odd += f(a + k*h)
        
    for k in range(2, N, 2):
        s_even += f(a + k*h)
        
    return (h/3)*(f(a) + f(b) + 4*s_odd + 2*s_even)
    
real_value = 4.4
i_value_10 = simpson(f, 0, 2, 10)
i_value_100 = simpson(f, 0, 2, 100)
i_value_1000 = simpson(f, 0, 2, 1000)

print('Real value: {0}, Simpson rule value for N = 10: {1}, Fract. difference: {2}'
        .format(real_value, i_value_10, np.abs((real_value - i_value_10) / real_value)))
print('Real value: {0}, Simpson rule value for N = 100: {1}, Fract. difference: {2}'
        .format(real_value, i_value_100, np.abs((real_value - i_value_100) / real_value)))
print('Real value: {0}, Simpson rule value for N = 1000: {1}, Fract. difference: {2}'
        .format(real_value, i_value_1000, np.abs((real_value - i_value_1000) / real_value)))