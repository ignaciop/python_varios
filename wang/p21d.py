import numpy as np
import matplotlib.pyplot as plt
import vpython as vp
import ode


def freefall (y, t):                  
    dydt = np.zeros(2)          
    dydt[0] = y[1]                
    dydt[1] = -g                   
    
    return dydt            

ball = vp.sphere(pos = vp.vector(0, 5, 0), radius = 1, color = vp.color.yellow)
floor = vp.box(pos = vp.vector(0, -5, 0), length = 8, height = 0.2, width = 4)

m = 1
t = 0
h = 0.01
v = 0.0
g = 9.8
pe = []
ke = []
tt = []


while (t <= 1):
    vp.rate(400)
    #y = ode.Euler(freefall, [ball.pos.y, v], t, h)
    y = ode.rk2(freefall, [ball.pos.y, v], t, h)
    t = t + h/2

    ball.pos.y = y[0]
    v = y[1]
    tt.append(t)
    pe.append(m*g*ball.pos.y)
    ke.append(0.5*m*v**2)

    if ball.pos.y > floor.pos.y + ball.radius:
        v = v - 9.8*h
    else:
        v = -v
    
    plt.figure()
    plt.plot(tt, pe, label = 'Potential Energy')
    plt.plot(tt, ke, label = 'Kinetic Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy')
    plt.grid()
    plt.legend(loc = 'best')
    plt.show()
