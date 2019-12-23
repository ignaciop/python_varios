import numpy as np
import matplotlib.pyplot as plt
import ode


def projectile(y, t):                  
    dydt = np.zeros(4)          
    dydt[0] = y[2]                
    dydt[1] = y[3]
    dydt[2] = 0                 
    dydt[3] = -g                  
                   
    return dydt            


t = 0
h = 0.01
x = 0
y = 0
vx = 10*np.cos(np.deg2rad(30))
vy = 10*np.sin(np.deg2rad(30))
g = 9.8

tt, posx, posy, velx, vely = [], [], [], [], []

while t <= 0.5:
    #y = ode.Euler(freefall, [ball.pos.y, v], t, h)
    yy = ode.rk2(projectile, [x, y, vx, vy], t, h)
    
    tt.append(t)
    posx.append(x)
    posy.append(y)
    velx.append(vx)
    vely.append(vy)

    x = yy[0]
    y = yy[1]
    vx = yy[2]
    vy = yy[3]
    t += h
    
    if y > -5.5:
        vy = vy - 9.8*h
    else:
        vy = -vy 

plt.figure()
plt.plot(tt, posx, label = 'x')
plt.plot(tt, posy, label = 'y')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.legend(loc = 'best')
plt.show()