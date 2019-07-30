import numpy as np
import matplotlib.pyplot as plt

def rolln(n):
    rolls = [np.random.randint(1, 7) for d in range(n)]
    
    return sum(rolls)
    
sums = [rolln(2) for d in range(10000)]
plt.figure()
plt.hist(sums, bins = 12, histtype = 'bar', color = 'gray')
plt.tight_layout()
plt.show()


sums = [rolln(3) for d in range(10000)]
plt.figure()
plt.hist(sums, bins = 18, histtype = 'bar', color = 'gray')
plt.tight_layout()
plt.show()