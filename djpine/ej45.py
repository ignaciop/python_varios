import numpy as np

f, a, da = np.loadtxt('ej44.txt', skiprows = 3, unpack = True)

print(f)
print(a)
print(da)

np.savetxt('ej45.csv', list(zip(f, a, da)), fmt = '%0.16e', 
            delimiter = ',')