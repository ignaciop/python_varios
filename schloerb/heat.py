import numpy as np
import matplotlib.pyplot as pl


dt = 10.;
tfinal = 3000.
dx = 10.;
alpha = dt/dx**2; 

x = np.linspace(0.,100.,100./dx+1)
t = np.linspace(0.,tfinal,tfinal/dt+1)

# V will hold the solution
V = np.zeros( (len(x),len(t)) )

# set boundary condition at x=100 for all times
V[len(x)-1,:] = 100; 
# note that initial condition is 0 everywhere except x=100

# now fill in the grid 
for j in range(len(t)-1):
    for i in range(1,len(x)-1):
        print(j,i)
        V[i,j+1] = V[i,j] + alpha*(V[i+1,j]-2*V[i,j]+V[i-1,j])

# plot the results for V(x) at different time steps
pl.figure()
pl.plot(x,V[:,0],'b',label='0') 
pl.plot(x,V[:,60],'m',label='60') 
pl.plot(x,V[:,120],'g',label='120') 
pl.plot(x,V[:,180],'c',label='180') 
pl.plot(x,V[:,240],'r',label='240') 
pl.plot(x,V[:,300],'k',label='300') 
pl.axis([-10.,110.,-10.,110.])
pl.grid()
pl.legend(loc=2)
pl.xlabel('X')
pl.ylabel('V')
pl.title('alpha = %5.2f'%(alpha))
pl.show()