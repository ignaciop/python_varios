import numpy as np
import matplotlib.pyplot as plt

d = np.array([0.38, 0.64, 0.91, 1.26, 1.41, 1.66, 1.90, 2.18])
f = np.array([1.4, 1.65, 3.0, 3.95, 4.3, 5.20, 6.85, 7.4])
df = np.array([0.4, 0.5, 0.4, 0.5, 0.6, 0.5, 0.5, 0.4])

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
    
slopew, yintw, ds, dds = lineFitWt(d, f, df)
rcsw = redchisq(d, f, df, slopew, yintw)


legendw = r'slope = {0:0.2f} $\pm$ {1:0.2f} N/cm\n intercept = {2:0.2f} $\pm$ {3:0.2f} N'.format(slopew,
            ds, yintw, dds)

plt.figure()
plt.errorbar(d, f, yerr = df, fmt = 'r.', ecolor = 'black', markersize = 10)
plt.plot(d, slopew*d + yintw, '-')
plt.plot(d, (slopew + ds)*d + yintw + dds, '--', color = 'gray')
plt.plot(d, (slopew - ds)*d + yintw - dds, '--', color = 'gray')
plt.text(0.50, 7.5, r'slope = {0:0.2f} $\pm$ {1:0.2f} N/cm'.format(slopew, ds))
plt.text(0.50, 7, r'intercept = {0:0.2f} $\pm$ {1:0.2f} N'.format(yintw, dds))
plt.xlabel('distance (cm)')
plt.ylabel('force (N)')
plt.tight_layout()
plt.show()