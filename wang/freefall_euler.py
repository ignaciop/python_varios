import numpy as np
import matplotlib.pyplot as plt
import ode

g = 9.8
	
def freefall(y, t):
	dydt = np.zeros(2)
	dydt[0] = y[1]
	dydt[1] = -g
	return dydt
	
def go(v0):
	y0 = [0.0, v0]
	t, h = 0.0, 0.02
	ta, ya, yb = [], [], []
	
	while t < 1.0:
		ta.append(t)
		ya.append(y0[0])
		yb.append(v0*t - g*t*t/2.0)
		y1 = ode.Euler(freefall, y0, t, h)
		
		for i in range(len(y0)):
			y0[i] = y1[i]
		t = t + h
		
	plt.figure()
	plt.plot(ta, ya, ta, yb, '--')
	plt.xlabel('t (s)')
	plt.ylabel('y (m)')
	plt.show()
	
go(5.0)