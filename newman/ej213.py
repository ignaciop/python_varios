def catalan(n):
    if n == 0:
        return 1
    else:
        return ((4*n - 2)/(n + 1))*catalan(n - 1)
        
def g(m, n):
    if n == 0:
        return m
    else:
        return g(n, m % n)

print(catalan(100))
print(g(108, 192))

