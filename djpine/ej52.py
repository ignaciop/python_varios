n = int(input('Input an integer > 1: '))
i = 2

while (n % i != 0):
    i += 1
    
if (i == n):
    print('{0:d} is a prime number'.format(n))
else:
    print('The smallest factor of {0:d} is {1:d}'.format(n, i))