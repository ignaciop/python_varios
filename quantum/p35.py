import numpy as np

N = int(input('N: '))
w = np.exp(-2*np.pi*1j/N)

Wt = np.ndarray((N, N), dtype = float)

for i in range(N):
    for j in range(N):
        Wt[i,j] = w**(i*j)

W = (1/np.sqrt(N))*Wt

np.savetxt('p35.txt', W, delimiter = ',')