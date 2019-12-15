import numpy as np
from sympy import *

t, lamb = symbols('t lamb', positive = True)
i = integrate(exp(-lamb*t), (t, 0, np.inf))

print(i)