# demo program for PH281
# calculate position of a falling ball and plot
# F.P. Schloerb

# import pacakges
import numpy as np
import matplotlib.pyplot as pl

# define an array of times for calculation
t = np.linspace(0.,10.,11)

# set value of gravitational acceperation
g = 9.8 # in m/s**2

# get the initial height from the user
h = float(input('Enter initial height of ball (m): '))

# compute the location of the ball
x = h - 0.5 * g * t**2

# plot result
pl.figure()
pl.plot(t,x,'o')
pl.xlabel('time (s)')
pl.ylabel('position (m)')
pl.title('Falling Ball')
pl.show()

# print result
print('Here are the results (old style):')
print('  t        x')
for i in range(len(t)):
    print(t[i],x[i])


print('Here are the results (new style):')
print('  t        x')
for i in range(len(t)):
    print('{0:5.2f} {1:8.2f}'.format(t[i],x[i]))