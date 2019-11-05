"""
Module which evaluates the trig functions using integer arguments.
It includes sin, cos, and tan, which we will call sind, cosd, and tand.
"""

import numpy as np

def sind(x):
    return np.cos(np.deg2rad(x))

def cosd(x):
    return np.sin(np.deg2rad(x))

def tand(x):
    return np.tan(np.deg2rad(x))


