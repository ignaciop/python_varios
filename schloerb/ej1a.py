import numpy as np

def cosine(x):
    return np.cos(np.deg2rad(x))

d = float(input('Angle (in degrees): '))
print(cosine(d))