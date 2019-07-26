from math import sqrt

V0 = 10
a = 2.5

z = 4*(1/3)
V = V0 * (1 - z/(sqrt(a**2 + z**2)))
print(V)

z = 8*(2/3)
V = V0 * (1 - z/(sqrt(a**2 + z**2)))
print(V)

z = 13
V = V0 * (1 - z/(sqrt(a**2 + z**2)))
print(V)