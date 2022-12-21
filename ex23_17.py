from sympy import *
import numpy as np
t = symbols('t')
func = sin(t) / t

expr = integrate(func, (t, 0, 2*np.pi))
expr2 = integrate(func, (t, 0, 2 * pi))
print(expr2, '=', expr)