import numpy as np

c0 = 1
i = 0

print(c0)

while True:
    c1 = int(((4*i + 2)/(i + 2))*c0)
    if c1 < 1e9:
        print(c1)
        c0 = c1
        i += 1
    else:
        break

