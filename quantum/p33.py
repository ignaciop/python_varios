from scipy.special import factorial
from numpy import exp

n = int(input('Numbers of terms: '))
x = float(input('x: '))
s = 0

rv = exp(x)

for i in range(n):
    s += (x**i)/factorial(i)

print('e^{0} for {1} terms: {2}'.format(x, n, s))
print('Numpy value for e^{0}: {1}'.format(x, rv))
