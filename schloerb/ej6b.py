from ej6a import trapezoidal

t0 = float(input('Lower limit: '))
t1 = float(input('Upper limit: '))

A = float(input('A: '))
B = float(input('B: '))
C = float(input('C: '))
D = float(input('D: '))
N = int(input('Step size: '))

def f(t):
    return A + B*t + C*t**2 + D*t**3

print(trapezoidal(f, t0, t1, N))


