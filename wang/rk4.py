def rk4(diffeq, y0, t, h):
	k1 = h*diffeq(y0, t)
	k2 = h*diffeq(y0 + 0.5*k1, t + h/2.)
	k3 = h*diffeq(y0 + 0.5*k2, t + h/2.)
	k4 = h*diffeq(y0 + k3, t + h)
	
	return y0 + (k1 + k4)/6.0 + (k2 + k3)/3.0