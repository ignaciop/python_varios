from numpy import sqrt as npsqrt

def isPrime(n):
    isTrue = True
    m = 2
    while m <= npsqrt(n):
        if n % m == 0:
            isTrue = False
            break
        m += 1
            
    return isTrue

primes = []
primes.append(2)

for x in range(3, 10001):
    if isPrime(x):
        primes.append(x)
        
print(primes)