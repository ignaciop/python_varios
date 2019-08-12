import numpy as np
import vpython as vp

rs = 695500
c1 = 10
r0_sun, t0_sun = 0, 0.01
r0_mercury, t0_mercury = 0.579, 0.88
r0_venus, t0_venus = 1.082, 2.247
r0_earth, t0_earth = 1.496, 3.653
r0_mars, t0_mars = 2.279, 6.87
r0_jupiter, t0_jupiter = 7.78, 43.316
r0_saturn, t0_saturn = 14.334, 107.592

vp.scene.autoscale = False

sun = vp.sphere(pos = vp.vector(r0_sun, 0, 0), color = vp.color.yellow, radius = 0.4)
mercury = vp.sphere(pos = vp.vector(r0_mercury, 0, 0), color = vp.color.orange, radius = 2440/rs*c1)
venus = vp.sphere(pos = vp.vector(r0_venus, 0, 0), color = vp.color.green, radius = 6052/rs*c1)
earth = vp.sphere(pos = vp.vector(r0_earth, 0, 0), color = vp.color.blue, radius = 6371/rs*c1)
mars = vp.sphere(pos = vp.vector(r0_mars, 0, 0), color = vp.color.red, radius = 3386/rs*c1)
jupiter = vp.sphere(pos = vp.vector(r0_jupiter, 0, 0), color = vp.color.orange, radius = 69173/rs*c1)
saturn = vp.sphere(pos = vp.vector(r0_saturn, 0, 0), color = vp.color.green, radius = 57316/rs*c1)

planets = [(sun, r0_sun, t0_sun), (mercury, r0_mercury, t0_mercury), 
            (venus, r0_venus, t0_venus), (earth, r0_earth, t0_earth), 
                (mars, r0_mars, t0_mars), (jupiter, r0_jupiter, t0_jupiter),
                    (saturn, r0_saturn, t0_saturn)]

theta = 0
while True:
    vp.rate(10)
    for p in planets:
        x = p[1]*np.cos(theta)
        y = p[1]*np.sin(theta)
        p[0].pos = vp.vector(x, y, 0)
        p[0].velocity = vp.vector(2*np.pi*p[1]*p[2], 2*np.pi*p[1]*p[2], 0)
    
    theta += 0.1
