def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n - 1)
        
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return int(factorial(n)/(factorial(k)*factorial(n - k)))
        
def probability(n, k):
    return binomial(n, k)/(2**n)
        
for n in range(1, 21):
    s = ''
    for k in range(0, n + 1):
        b = binomial(n, k)
        s += str(b) + ' '
    print(s)
    
p = probability(100, 60)
pm = 1 - p

print('Probability of a coin tossed 100 times comes up heads exactly 60 times: ', p)
print('Probability of a coin tossed 100 times comes up heads 60 or more times: ', pm)