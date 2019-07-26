f = 1
i = 1

print('Using while loop...\n')
n = int(input('Positive integer: '))

while (i <= n):
    f *= i
    i += 1
    
print('{0}!: {1}'.format(n, f))

f = 1

print('Using for loop...\n')
n = int(input('Positive integer: '))

for i in range(1,n+1):
    f *= i
    
print('{0}!: {1}'.format(n, f))