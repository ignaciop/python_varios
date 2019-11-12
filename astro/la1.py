import numpy as np
import scipy.linalg as sp

theta = np.deg2rad(35)
m = 14
l = 1.2
g = 9.8

A = np.array([[1, 0, -np.cos(theta)], [0, 1, np.sin(theta)], [0, -l/2, l*np.sin(theta)/2]])
r = np.array([[0], [m*g], [0]])

f = sp.solve(A, r)

print(f)