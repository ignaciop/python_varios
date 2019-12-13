from cmath import sqrt

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

r1 = (2*c)/(-b - sqrt(b**2 - 4*a*c))
r2 = (2*c)/(-b + sqrt(b**2 - 4*a*c))

print('Roots of {0}*x^2 + {1}*x + {2}: {3}, {4}'.format(a, b, c, r1, r2))