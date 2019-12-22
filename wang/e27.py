import numpy as np
from sympy import *

t, lamb = symbols('t lamb', positive = True)
integrate(exp(-lamb*t), (t, 0, np.inf))

1/lamb
