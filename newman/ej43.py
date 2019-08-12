def f(x):
    return x*(x - 1)
    
def dfdx(delta, x = 1):
    return (f(x + delta) - f(x))/delta
    
print(dfdx(1e-2))
print(dfdx(1e-4))
print(dfdx(1e-6))
print(dfdx(1e-8))
print(dfdx(1e-10))
print(dfdx(1e-12))
print(dfdx(1e-14))