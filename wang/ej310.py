from sympy import *

x, a = symbols('x a')
s = solve(x**x - a, x)

print(s)

R, vx, b, g, vy = symbols('R, vx, b, g, vy')
ss = solve((R - vx/b)*exp((b**2*vy/(g*vx) + b/vx)*R) + vx/b, R)

print(ss)