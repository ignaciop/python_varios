import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

N = 50
l = 1
coseno = lambda t: np.cos((t**2)*np.pi/2) 
seno = lambda t: np.sin((t**2)*np.pi/2) 

xx = np.linspace(-5, 5, 500)
zz = 3
uu = xx*np.sqrt(2/(l*zz))

x, w = gaussxw(N)

def C(u_):
	
	a = 0
	b = u_
	xp = 0.5*(b - a)*x + 0.5*(b + a)
	wp = 0.5*(b - a)*w
	E = coseno(u_)
	
	y = coseno(xp)
	s = sum(y*wp)

	return s
	
def S(u_):

	a = 0
	b = u_
	xp = 0.5*(b - a)*x + 0.5*(b + a)
	wp = 0.5*(b - a)*w
	E = seno(u_)

	y = seno(xp)
	s = sum(y*wp)

	return s
	
def I(u):
 return (1/8)*((2*C(u) + 1)**2 + (2*S(u) + 1)**2)

I = [I(u) for u in uu]
plt.figure()
plt.plot(xx, I)
plt.xlabel('x (m)')
plt.ylabel('$I/I_0$')
plt.grid()
plt.show()