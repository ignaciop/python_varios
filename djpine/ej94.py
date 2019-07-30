import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

def gaussNoisy(x, noiseAmp):
    noise = noiseAmp*(np.random.randn(len(x)))
    
    return np.exp(-0.5*x*x)*(1.0 + noise)
    
N = 256
x = np.linspace(-4.0, 4.0, N)
y = gaussNoisy(x, 0.1)
dx = x[1] - x[0]

G = fftpack.fft(y)
f = fftpack.fftfreq(y.size, d = dx)
f = fftpack.fftshift(f)
G = fftpack.fftshift(G)


plt.rc('mathtext', fontset = 'stix')
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (9, 6))
ax1.plot(x, y)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y(x)$')

ax2.plot(f, np.real(G), color = 'dodgerblue', label = 'real part')
ax2.plot(f, np.imag(G), color = 'coral', label = 'imaginary part')
ax2.legend()
ax2.set_xlabel(r'$f$')
ax2.set_ylabel(r'$G(f)$')

Ginv = fftpack.ifft(G)
ax3.plot(x, np.real(Ginv)**2, color = 'red', label = 'retransformed signal')
ax3.plot(x, y, label = 'original')
ax3.legend()
ax3.set_xlabel(r'$f$')
ax3.set_ylabel(r'$y(x)$')

plt.tight_layout()
plt.show()

