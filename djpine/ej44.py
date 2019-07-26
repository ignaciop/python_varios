import numpy as np

f, a, da = np.loadtxt('ej43.txt', skiprows = 3, unpack = True)

print(f)
print(a)
print(da)

header = 'Date: 2013-09-16'
header += '\nData taken by Liam and Serena'
header += '\nfrequency (Hz) amplitude (mm) amp error (mm)'

np.savetxt('ej44.txt', list(zip(f, a, da)), header = header,
            fmt = '%12.4f')