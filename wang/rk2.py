def RK2(diffeq, y0, t, h):
	k1 = h*diffeq(y0, t)
	k2 = h*diffeq(y0 + 0.5*k1, t + h/2.)
	
	return y0 + k2