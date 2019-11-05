import numpy as np

Ainv = np.array([[1, 4, 2], [3, 6, 8], [5, 8, 9]])
b = np.array([1, 4, 7])

x = np.dot(Ainv, b)
print(x)