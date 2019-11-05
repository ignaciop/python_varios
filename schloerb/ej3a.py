# demo program for PH281
# calculate position of a falling ball and plot
# F.P. Schloerb

# import pacakges
import numpy as np
import matplotlib.pyplot as plt

# define an array of times for calculation
t = np.linspace(0.,10.,11)
xx = []

# set value of gravitational acceperation
g = 9.8 # in m/s**2

# get the initial height from the user
h = float(input('Enter initial height of ball (m): '))

# compute the location of the ball
for ts in t:
    x = h - 0.5 * g * ts**2

    if x <= 0:
        break
    
    xx.append(x)
    
tt = t[0:len(xx)]

# plot result
plt.figure()
plt.plot(tt,xx,'o')
plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.title('Falling Ball')
plt.show()


print('Here are the results (new style):')
print('  t        x')
for i in range(len(tt)):
    print('{0:5.2f} {1:8.2f}'.format(tt[i],xx[i]))