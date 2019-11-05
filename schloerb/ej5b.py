import numpy as np

def inter(tp):
    i = 0
    t, y = np.loadtxt('table.dat', unpack = True)

    if tp < t[0] or tp > t[-1]:
        raise ValueError('Value not in t')
    else:
        while(i < len(t)):
            if t[i] <= tp and t[i + 1] >= tp:
                yy = ((tp - t[i])*(y[i + 1] - y[i]))/(t[i + 1] - t[i]) + y[i]
                break
            
            i += 1
        return yy

print(inter(12.34))