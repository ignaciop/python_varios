import matplotlib.pyplot as plt
import ode
import math as ma

def oscillator(id, x, v, t):
	if (id == 0):
		return v
	else:
		return -x
		
def go():
	x, v = 1.0, 0.0
	t, h = 0.0, 0.1
	xa, va = [], []
	
	while t < 4*ma.pi:
		xa.append(x)
		va.append(v)
		x, v = ode.leapfrog(oscillator, x, v, t, h)
		t = t + h
		
	plt.figure()
	plt.plot(xa, va)
	plt.xlabel('x (m)')
	plt.ylabel('v (m/s)')
	plt.show()
	
go()

