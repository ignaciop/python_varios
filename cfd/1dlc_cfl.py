import numpy as np
import matplotlib.pyplot as plt
import time, sys

def linearconv(nx):
    dx = 2/(nx - 1)
    nt = 25
    c = 1
    sigma = .5
    dt = sigma*dx

    u = np.ones(nx)
    u[int(.5/dx):int(1/dx + 1)] = 2
    print(u)

    un = np.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - c*dt/dx*(un[i] - un[i - 1])
        
    plt.plot(np.linspace(0, 2, nx), u)
    plt.show()
    
linearconv(101)