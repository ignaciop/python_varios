import numpy as np
import matplotlib.pyplot as plt

def lineFit(x, y):
    xavg = x.mean()
    slope = sum((y * (x - xavg))) / sum(x * xavg)
    yint = y.mean() - slope * xavg
    
    return slope, yint
    
def lineFitWt(x, y, dy):
    """
    Fit to straight line.
    Inputs: x, y, and dy (y-uncertainty) arrays.
    Ouputs: slope and y-intercept of best fit to data.
    """
    dy2 = dy ** 2
    norm = (1. / dy2).sum()
    xhat = (x / dy2).sum() / norm
    yhat = (y / dy2).sum() / norm
    slope = ((x - xhat) * y / dy2).sum() / ((x - xhat) * x / dy2).sum()
    yint = yhat - slope * xhat
    dy2_slope = 1. / ((x - xhat) * x / dy2).sum()
    dy2_yint = dy2_slope * (x * x / dy2).sum() / norm
    return slope, yint, np.sqrt(dy2_slope), np.sqrt(dy2_yint)


def redchisq(x, y, dy, slope, yint):
    chisq = (((y - yint - slope * x) / dy) ** 2).sum()
    return chisq / float(x.size - 2)
    
t, v, u = np.loadtxt('ej73.txt', skiprows = 2, unpack = True)

slope, yint = lineFit(t, v)
slopew, yintw, d, dd = lineFitWt(t, v, u)
rcs = redchisq(t, v, u, slope, yint)
rcsw = redchisq(t, v, u, slopew, yintw)

legend = r'Without weights: a = {0:0.2f}, b = {1:0.2f}, $\chi 2$ = {2:0.5f}'.format(yint,
            slope, rcs)
legendw = r'With weights: a = {0:0.2f}, b = {1:0.2f}, $\chi 2$ = {2:0.5f}'.format(yintw,
            slopew, rcsw)

plt.figure()
plt.errorbar(t, v, yerr = u, fmt = 'g.', ecolor = 'black')
plt.plot(t, slope*t + yint, '-')
plt.plot(t, slopew*t + yintw, '-')
plt.legend([legend, legendw], loc = 'best')
plt.axhline(color = 'gray', linestyle = '--', zorder = -1)
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.tight_layout()
plt.show()