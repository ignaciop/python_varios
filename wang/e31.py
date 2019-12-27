import numpy as np
import vpython as vp
import ode


def projectile(y, t):                  
    dydt = np.zeros(4)          
    dydt[0] = y[2]                
    dydt[1] = y[3]
    dydt[2] = 0                 
    dydt[3] = -g                  
                   
    return dydt            

ball = vp.sphere(pos = vp.vector(-4, -4, 0), radius = 1, color = vp.color.yellow)
floor = vp.box(pos = vp.vector(0, -5, 0), length = 12, height = 0.2, width = 4)
path = vp.points(pos = ball.pos)

t = 0
h = 0.01
vx = 4.0
vy = 9.8
g = 9.8

while True:
    vp.rate(200)
    #y = ode.Euler(freefall, [ball.pos.y, v], t, h)
    y = ode.rk2(projectile, [ball.pos.x, ball.pos.y, vx, vy], t, h)
    
    ball.pos.x = y[0]
    ball.pos.y = y[1]
    vx = y[2]
    vy = y[3]

    path.append(pos=ball.pos, retain=300)

    if ball.pos.y > floor.pos.y + ball.radius:
        vy = vy - g*h
    else:
        vy = -vy
        vx = -vx