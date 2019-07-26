from cmath import sqrt

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

a = a + 0j

x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(x1, x2)