import numpy as np
import scipy.linalg as sp


v = np.array([[12], [9]])
R = np.array([[100, 65], [-120, 65]])

i = sp.solve(R, v)

print(i)