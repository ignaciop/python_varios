import numpy as np
import vpython as vp

vp.graph(width = 400, height = 250, title = '<i>x,y movement</i>', 
            xtitle='<i>t</i>', ytitle='<i>x = rcos(theta), y = rsin(theta)</i>',
                background = vp.color.white)
xDots = vp.gdots(color = vp.color.green)
yDots = vp.gdots(color = vp.color.magenta)

vp.canvas(background = vp.vector(0.7, 0.7, 0.7))
s = vp.sphere(pos = vp.vector(0, 0, 0), radius = 0.01,
                color = vp.vector(0.2, 0.4, 0.9), opacity = 0.6,
                 make_trail = True, interval = 10,
                    trail_color = vp.color.orange)
                
theta = vp.radians(0)
r = s.radius
i = 0
j = 1
t = 0

while True:
    vp.rate(20)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    s.pos = vp.vector(x, y, 0)
    theta += vp.radians(1)     
        
    print('{0:d} loops'.format(i))
    
    if i != 0 and i % vp.degrees(2*np.pi) == 0:
        print('{0:d} orbits completed'.format(j))
        j += 1
        
    i += 1
    
    t += 1
    xDots.plot(t, x)
    yDots.plot(t, y)