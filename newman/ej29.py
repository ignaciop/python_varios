import numpy as np

e = 1.6022e-19
e0 = 8.8542e-12
a = 2.82e-10
V_total = 0

L = int(input('L: '))

for i in range(-L, L):
    for j in range(-L, L):
        for k in range(-L, L):
            if i != 0 and j != 0 and k != 0:
                if (i + j + k) % 2 == 0:
                    V_total -= e/(4*np.pi*e0*a*np.sqrt(i**2 + j**2 + k**2))
                else:
                    V_total += e/(4*np.pi*e0*a*np.sqrt(i**2 + j**2 + k**2))
                    
M = 4*np.pi*e0*a*V_total/e

print(M)