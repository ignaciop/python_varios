import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

N = 100
m = 1
V = lambda x: x**4

x,w = gaussxw(N)


def T(a_):
	
	a = 0
	b = a_
	xp = 0.5*(b - a)*x + 0.5*(b + a)
	wp = 0.5*(b - a)*w
	E = V(a_)
	
	y = 1/np.sqrt(E - V(xp))
	s = sum(y*wp)

	return s*np.sqrt(8*m)
	
a = np.linspace(0,2,100)
periods = [T(ai) for ai in a]

plt.figure()
plt.plot(a, periods)
plt.xlabel('initial position')
plt.ylabel('period')
plt.show()