import numpy as np
import matplotlib.pyplot as plt

N = 51
ymas, ymenos = np.empty(N), np.empty(N)
err_mas, err_menos = np.empty(N), np.empty(N)
phi_mas = ((1 + np.sqrt(5))/2)
phi_menos = ((1 - np.sqrt(5))/2)
ymas[50], ymenos[50] = 1, phi_menos
ymas[49], ymenos[49] = phi_mas, 1
err_mas[50], err_menos[50] = 0, 0
err_mas[49], err_menos[49] = 0, 0

for n in reversed(range(N - 1)):
    ymenos[n-1] = -ymenos[n] + ymenos[n+1]
    ymas[n-1] = -ymas[n] + ymas[n+1]

ymenos = [ymenos[i]/ymenos[0] for i in range(N)]
ymas = [ymas[i]/ymas[0] for i in range(N)]
nn = [i for i in range(N)]

for n in reversed(range(N-1)):
    err_menos[n-1] = np.abs(ymenos[n-1] - phi_menos**(n-1))/np.abs(phi_menos**(n-1))
    err_mas[n-1] = np.abs(ymas[n-1] - phi_mas**(n-1))/np.abs(phi_mas**(n-1))


plt.figure(1)
plt.semilogy(nn,err_mas, label=r'$\phi_{-} = \frac{1 + \sqrt{5}}{2}$')
plt.semilogy(nn,err_menos, label=r'$\phi_{-} = \frac{1 - \sqrt{5}}{2}$')
plt.xlabel(r'$n$')
plt.ylabel('Relative error')
plt.xticks()
plt.yticks()
plt.legend(fontsize=18)
plt.show()