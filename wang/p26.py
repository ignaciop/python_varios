import numpy as np
import matplotlib.pyplot as plt
import ode

lh = 2.0
lz = 1.0

def zh_ode(y, t):                  
    dydt = np.zeros(2)          
    dydt[0] = -lz*y[1]
    dydt[1] = -lh*y[0]
    
    return dydt 


def go(humans, zombies):

    t, h = 0.0, 0.1
    tt = []
    
    humans_array, zombies_array = [], []

    while (humans >= 0 and zombies >=0):
        
        humans_array.append(humans)
        zombies_array.append(zombies)

        humans_zombies_ode = ode.rk4(zh_ode, [humans, zombies], t, h)

        humans = humans_zombies_ode[0]
        zombies = humans_zombies_ode[1]

        tt.append(t)
        t += h


    plt.figure()
    plt.plot(tt, humans_array, '.', label = 'Humans')
    plt.plot(tt, zombies_array, '.', label = 'Zombies')
    plt.xlabel('Time (s)')
    plt.ylabel('H, Z')
    plt.legend(loc = 'best')
    plt.title('At $t = 0$, H = {0} and Z = {1} '.format(humans_array[0], zombies_array[0]))
    plt.show()

    plt.figure()
    plt.plot(humans_array, zombies_array)
    plt.xlabel('H')
    plt.ylabel('Z')
    plt.legend(loc = 'best')
    plt.title('At $t = 0$, H = {0} and Z = {1} '.format(humans_array[0], zombies_array[0]))
    plt.show()
    

go(70, 99)
go(69, 100)

for h in [80, 100, 120]:
    go(h, 99)
