import numpy as np
import vpython as vp
import ode


def freefall (y, t):                  
    dydt = np.zeros(2)          
    dydt[0] = y[1]                
    dydt[1] = -g                   
    
    return dydt            

ball = vp.sphere(pos = vp.vector(0, 5, 0), radius = 1, color = vp.color.yellow)
floor = vp.box(pos = vp.vector(0, -5, 0), length = 8, height = 0.2, width = 4)

t = 0
h = 0.01
v = 0.0
g = 9.8

while True:
    vp.rate(400)
    #y = ode.Euler(freefall, [ball.pos.y, v], t, h)
    y = ode.rk2(freefall, [ball.pos.y, v], t, h)
    
    ball.pos.y = y[0]
    v = y[1]
    
    if ball.pos.y > floor.pos.y + ball.radius:
        v = v - 9.8*h
    else:
        v = -v 