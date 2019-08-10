import numpy as np
from operator import itemgetter

A = 58
Z = 28

def B(A, Z):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2
    
    if A % 2 != 0:
        a5 = 0
    elif A % 2 == 0 and Z % 2 == 0:
        a5 = 12.0
    else:
        a5 = -12
    
    B = a1*A - a2*A**(2/3) - a3*Z**2/A**(1/3) - a4*(A - 2*Z)**2/A + a5/A**(1/2)
    
    return B

def stable_nucleus(Z):
    Aes = []

    for A in range(Z, 3*Z):
        baz = B(A, Z)
        Aes.append((A, baz/A))

    stable_nucleus = max(Aes,key = itemgetter(1))

    return stable_nucleus


print('Binding energy for A = {0} and Z = {1}: {2:0.2f} MeV'.format(A, Z, B(A, Z)))
print('Binding energy per nucleon for A = {0} and Z = {1}: {2:0.2f} MeV'
        .format(A, Z, B(A, Z)/A))
print('Stable nucleus --> A = {0}, B/A = {1:0.2f} MeV'.format(stable_nucleus(Z)[0], stable_nucleus(Z)[1]))

for Z in range(1, 101):
    print('Stable nucleus for Z = {0} --> A = {1}, B/A = {2:0.2f} MeV'.format(Z, stable_nucleus(Z)[0], stable_nucleus(Z)[1]))