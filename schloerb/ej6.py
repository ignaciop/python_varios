from ej6a import *

def f(t):
    return 4 - 2*t + 6*t**2


print(rectangle(f, 0, 10, 500000))
print(trapezoidal(f, 0, 10, 100000))
print(simpson(f, 0, 10))