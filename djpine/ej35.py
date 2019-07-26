import numpy as np

a = np.zeros((8,8), dtype = int)
a[0][:] = a[len(a)-1][:] = 1
a[1::, ::len(a)-1] = a[::len(a)-1, 1::] = 1

print(a)

b = np.zeros((8, 8), dtype = int) 
b[1::2, ::2] = 1
b[::2, 1::2] = 1

print(b)

c = np.arange(2,50,5)
print(c)
c[c % 3 != 0] = -1*c[c % 3 != 0]
print(c)

print(np.size(a))
print(np.size(b))
print(np.size(c))

print(np.mean(a))
print(np.mean(b))
print(np.mean(c))

print(np.std(a))
print(np.std(b))
print(np.std(c))