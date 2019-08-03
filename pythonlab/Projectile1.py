import numpy as np
import vpython as vp

g = 9.81
dt = 0.005
t = 0
vy = 0

vp.canvas(background = vp.vector(0.7, 0.7, 0.7))

f = vp.box(pos = vp.vector(0, 0, 0), length = 2, width = 2,
                height = 0.1, color = vp.color.orange)
                
s = vp.sphere(pos = vp.vector(f.pos.x, 10 + f.pos.y, f.pos.z),
                radius = 0.25, color = vp.vector(0.2, 0.4, 0.9),
                    trail_type = 'points', make_trail = True,
                        trail_color = vp.color.green)

vp.scene.center = vp.vector(0, s.pos.y/2, 0)
vp.scene.width = 400
         
while s.pos.y > s.radius + f.height:
    vp.rate(100)
    ay = -g
    s.pos.y += vy*dt
    vy += ay*dt
    t += dt
    
print(s.pos.y/vy)
print('Ball lands at t = ', t, ' seconds, with velocity ', vy, ' m/s')
print(s.pos.y)