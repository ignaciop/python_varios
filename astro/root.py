import numpy as np

def bisection(f, a, b, tol = 1e-6):
    if f(a)*f(b) > 0:
        #end function, no root.
        print("No root found.")
    else:
        while (b - a)/2.0 > tol:
            midpoint = (a + b)/2.0

            if f(midpoint) == 0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        
        return midpoint

def function(x):
  return x * (x + 2) - 1

def functionDerivative(x):
  return 2 * x + 2

def newton(f, df, x0, tol = 1e-6):
    x = x0
    prevX = x0

    while(abs(f(x)) > tol):
        print("X: ", x, " f(x): ", f(x))
        x = prevX - (f(prevX) / df(prevX))
        prevX = x

    return x

x = lambda t: (vx0/k)*(1 - np.exp(-k*t))
T = lambda t: ((k*vy0 + g)/(g*k))*(1 - np.exp(-k*t))
dT = lambda t: ((k*vy0 + g)/(g*k))*(1 - np.exp(-k*t))*(k*t)

v0 = 100
theta = np.deg2rad(45)
k = 0.01
vx0 = v0*np.cos(theta)
vy0 = v0*np.sin(theta)
g = 9.81

t = bisection(T, 0, 1)
tt = newton(T, dT, 1) 

print('Bisection method: Landing time (s): ', t, '\nDistance (cm): ', x(t))
print('Newton method: Landing time (s): ', tt, '\nDistance (cm): ', x(tt))