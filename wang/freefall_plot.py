import matplotlib.pyplot as plt

g, h = 9.8, 0.02
y, v0 = 0.0, 5.0
ta, ya = [], []
t, yb = 0.0, []

while t < 1.0:
	ta.append(t)
	ya.append(y)
	yb.append(v0*t - g*t*t/2.0)
	v = v0 - g*t
	y = y + v*h
	t = t + h
	
plt.figure()
plt.plot(ta, ya, ta, yb, '--')
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()