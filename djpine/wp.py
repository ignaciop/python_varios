import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def ww(x, t, k0, a0, vp, vg):
    tc = a0*a0*1j*(0.5*vg/k0)*t
    u = np.exp(1.0j*k0*(x - vp*t) - 0.25*(x - vg*t)**2/tc)
    
    return np.real(u/np.sqrt(tc))
    
wavelength = 1.0
a0 = 1.0
k0 = 2*np.pi/wavelength
vp, vg = 5.0, 10.0
period = wavelength/vp
runtime = 40*period
rundistance = 0.6*vg*runtime
dt = period/6.0
tsteps = int(runtime/dt)

fig, ax = plt.subplots(figsize = (12, 3))
fig.subplots_adjust(bottom = 0.2)
x = np.arange(-5*a0, rundistance, wavelength/20.0)
line = ax.plot(x, np.ma.array(x, mask = True), color = 'C0')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x,t)$')
ax.set_xlim(-5*a0, rundistance)
ax.set_ylim(-1.05, 1.05)

def animate(i):
    t = float(i)*dt
    line.set_ydata(ww(x, t, k0, a0, vp, vg))
    return line
    
ani = anim.FuncAnimation(fig, func = animate, frames = range(tsteps),
                            interval = 1000*dt, blit = True)
fig.show()