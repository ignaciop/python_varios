import numpy as np

g = 9.8
h0 = 10

y = np.arange(10, 0, -0.5)
t = np.sqrt(2*(h0 - y)/g)

print(y)
print(t)
print(list(zip(t, y)))