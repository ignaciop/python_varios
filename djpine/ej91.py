import numpy as np
import scipy.linalg

A = np.array([[1, -2, 9, 13], [-5, 1, 6, -7], [4, 8, -4, -2],
                [8, 5, -7, 1]])
b = np.array([1, -3, -2, 5])

x = scipy.linalg.solve(A, b)
print(x)