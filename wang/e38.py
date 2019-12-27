import rootfinder as rtf
from scipy.optimize import fsolve

def f(x):
    return 5*x - x**3

def df(x):
    return 5 - 3*x**2

a, b = -2, 2

bs = rtf.bisect(f, a, b)
nt = rtf.newton(f, df, a)

print(bs)
print(nt)

x = fsolve(f, -2)
print(x)

