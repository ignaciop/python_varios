import numpy as np
import scipy.linalg as sp



M = np.array([[1, 3], [4, 2]])

values, vectors= sp.eig(M)

first_eigenvector = vectors[:,0]/np.abs(vectors[:,0])
second_eigenvector = vectors[:,1]/np.abs(vectors[:,1])

print('Eigenvalue = ', values[0],', Eigenvector (normalized): ', first_eigenvector)
print('Eigenvalue = ', values[1],', Eigenvector (normalized): ', second_eigenvector)