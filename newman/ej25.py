import numpy as np

m = 9.11e-31
hbar = 6.63e-34
E = 10
V = 9

k1 = np.sqrt(2 * m * E) / hbar
k2 = np.sqrt(2 * m * (E - V)) / hbar

T = (4 * k1 * k2) / ((k1 + k2)**2)
R = ((k1 - k2) / (k1 + k2))**2

print('Transmission coefficient: {0:.2f}\nReflection coefficient: {1:.2f}'.
        format(T, R))