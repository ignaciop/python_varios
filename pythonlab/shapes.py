import vpython as vp

b1 = vp.box(pos = vp.vector(0, 8, 0), size = vp.vector(0.5, 0.5, 0.5),
        color = vp.vector(0.4, 0.1, 0.6))
        
# Clone copia la figura referenciada pero podemos elegir otros
# parametros, por ejemplo la posicion. Lo demas queda igual 
   
b2 = b1.clone(pos = vp.vector(-5, 5, 0), 
                color = vp.vector(0.29, 0.5, 0.8))
b3 = b1.clone(pos = vp.vector(5, 5, 0), 
                color = vp.vector(0.27, 0.76, 0.72))

s1 = vp.sphere(pos = vp.vector(5, 5, 5), radius = 0.25,
                color = vp.color.red)
s2 = s1.clone(pos = vp.vector(5, 5, -5), color = vp.color.yellow)

c1 = vp.cylinder(pos = vp.vector(-5, 5, -5), 
                    axis = vp.vector(0, 1.5, 0),
                        color = vp.color.orange)
       
# Creo los ejes de referencias (canonicos)
                
exp = vp.cylinder(pos = vp.vector(0, 0, 0), 
                    axis = vp.vector(5, 0, 0), radius = 0.05, 
                        color = vp.vector(0.6, 0.6, 0.6))
exn = exp.clone(axis = vp.vector(-5, 0, 0))
eyp = vp.cylinder(pos = vp.vector(0, 0, 0), 
                    axis = vp.vector(0, 5, 0), radius = 0.05, 
                        color = vp.vector(0.6, 0.6, 0.6))
eyn = eyp.clone(axis = vp.vector(0, -5, 0))
ezp = vp.cylinder(pos = vp.vector(0, 0, 0), 
                    axis = vp.vector(0, 0, 5), radius = 0.05, 
                        color = vp.vector(0.6, 0.6, 0.6))
ezn = ezp.clone(axis = vp.vector(0, 0, -5))
                        