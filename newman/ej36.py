import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r*x*(1 - x)

n = 1000
r = np.linspace(1, 4, n)

iterations = 1000
last = 100

x = 0.5*np.ones(n)

plt.figure(figsize = (9, 5))
for i in range(iterations):
    x = logistic(r, x)

    # We display the bifurcation diagram.
    if i >= (iterations - last):
        plt.plot(r, x, ',k', alpha = .25)
plt.xlim(1, 4)
plt.title("Bifurcation diagram")
plt.show()


