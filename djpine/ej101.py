import numpy as np
import pandas as pd

planets = pd.read_table('planetData.txt', sep = '\s+')
print(planets)

avg_dens = []
for d in planets:
    vol = 4/3*(np.pi*(d.diameter/2)**3)
    avg_dens_p = d/vol
    avg_dens.append(avg_dens_p)
    
print(avg_dens)