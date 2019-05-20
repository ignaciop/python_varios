def Euler(diffeq, y0, t, h):
	dydt = diffeq(y0, t)
	return y0 + h*dydt

	
def rk2(diffeq, y0, t, h):
	k1 = h*diffeq(y0, t)
	k2 = h*diffeq(y0 + 0.5*k1, t + h/2.)

	return y0 + k2

	
def rk4(diffeq, y0, t, h):
	k1 = h*diffeq(y0, t)
	k2 = h*diffeq(y0 + 0.5*k1, t + h/2.)
	k3 = h*diffeq(y0 + 0.5*k2, t + h/2.)
	k4 = h*diffeq(y0 + k3, t + h)

	return y0 + (k1 + k4)/6.0 + (k2 + k3)/3.0

	
def rk4n(diffeq, y0, t, h):
	n, y1 = len(y0), [0,0]*len(y0)
	k1 = diffeq(y0, t)
	for i in range(n):
		y1[i] = y0[i] + 0.5*h*k1[i]
	
	k2 = diffeq(y1, t + h/2.)
	for i in range(n):
		y1[i] = y0[i] + 0.5*h*k2[i]
		
	k3 = diffeq(y1, t + h/2.)
	for i in range(n):
		y1[i] = y0[i] + h*k3[i]
		
	k4 = diffeq(y1, t + h)
	for i in range(n):
		y1[i] = y0[i] + h*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6.0
		
	return y1


def RK45n(diffeq, y0, t, h):
	a2, a3, a4, a5, a6 = 0.2, 0.3, 0.6, 1.0, 0.875
	b21, b31, b32, b41, b42, b43 = 0.2, 3./40., 9./40., 0.3, -0.9, 1.2
	b51, b52, b53, b54 = -11./54., 2.5, -70./27., 35./27.
	b61, b62, b63, b64, b65 = [1631./55296., 175./512., 575./13824., 44275./110592., 253./4096.]
	c1, c3, c4, c6 = 37./378., 250./621., 125./594., 512./1771.

	n, y1 = len(y0), [0.0]* len(y0)
	k1 = diffeq(y0, t)
	for i in range(n):
		y1[i] = y0[i] + h*b21*k1[i]
		
	k2 = diffeq(y1, t + a2*h)
	for i in range(n):
		y1[i] = y0[i] + h*(b31*k1[i] + b32*k2[i])
		
	k3 = diffeq(y1, t + a3*h)
	for i in range(n):
		y1[i] = y0[i] + h*(b41*k1[i] + b42*k2[i] + b43*k3[i])
		
	k4 = diffeq(y1, t + a4*h)
	for i in range(n):
		y1[i] = y0[i] + h*(b51*k1[i] + b52*k2[i] + b53*k3[i] + b54*k4[i])
		
	k5 = diffeq(y1, t + a5*h)
	for i in range(n):
		y1[i] = y0[i] + h*(b61*k1[i] + b62*k2[i] + b63*k3[i] + b64*k4[i] + b65*k5[i])
		
	k6 = diffeq(y1, t + a6*h)
	for i in range(n):
		y1[i] = y0[i] + h*(c1*k1[i] + c3*k3[i] + c4*k4[i] + c6*k6[i])
		
	return y1


def leapfrog(lfdiffeq, r0, v0, t, h):
	hh = h/2.0
	r1 = r0 + hh*lfdiffeq(0, r0, v0, t)         
	v1 = v0 + h* lfdiffeq(1, r1, v0, t + hh) 
	r1 = r1 + hh*lfdiffeq(0, r0, v1, t + h)     
	return r1, v1