import numpy as np

a = np.exp(1)*np.ones(100)
print(a)

b = np.arange(0,361,1)
print(b)

c = b*np.pi/180
print(c)

print(c-b*np.pi/180)

d = np.arange(12,17,0.2)
print(d)

e = np.arange(12,17.2,0.2)
print(e)