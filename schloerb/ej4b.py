from math import sqrt

def f(x):
    return x**2 - 2

def bisection(f, a, b, tol, nmax):
    n = 1
    while (n <= nmax):
        c = (a + b) / 2
        print('Iteration: ', n, ', midpoint: ', c)
        if (f(c) == 0 or (b - a) / 2 < tol):
            return c

        n += 1

        if (f(c) - f(a) >= 0):
            a = c
        else:
            b = c

x = bisection(f, 1.4, 1.5, 1e-4, 10000)
print('Root is: ', x)
print('Actual value is: ', sqrt(2))
            