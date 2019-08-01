import vpython as vp


bar = vp.cylinder(pos = vp.vector(0, 0, 0), radius = 0.05, 
                    axis = vp.vector(1, 0, 0),
                        color = vp.color.orange)


s1 = vp.sphere(pos = bar.pos, radius = bar.radius*3,
                color = bar.color)
s2 = s1.clone(pos = bar.pos + bar.axis)
