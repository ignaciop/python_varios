import numpy as np

G = 6.67e-11
M = 5.97e24
R = 6371000

T = float(input('Period (seconds): '))

h = lambda T : np.abs(((G * M * T**2) / (4 * np.pi**2))**(1/3) - R)

print('Altitude above Earth\'s surface for T = {0:0.2f} seconds: {1:0.2f} meters'.
        format(T, h(T)))
        
# 90 minutes = 5400 seconds
T = 5400
print('Altitude above Earth\'s surface for T = 90 minutes: {0:0.2f} meters'.
        format(h(T)))
        
# 45 minutes = 2700 seconds
T = 2700
print('Altitude above Earth\'s surface for T = 45 minutes: {0:0.2f} meters'.
        format(h(T)))
        
T = 86148
print('Altitude above Earth\'s surface for T = 23.93 hours: {0:0.2f} meters'.
        format(h(T)))
        
T = 86400
print('Altitude above Earth\'s surface for T = 24 hours: {0:0.2f} meters'.
        format(h(T)))