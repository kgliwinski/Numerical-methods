from sympy import *
import numpy as np
x = symbols('x')
func = 1 / sqrt(2*pi) * exp(-x**2 / 2)
# func_np = 1 / sqrt(2*np.pi) * exp(-x**2 / 2)
print(integrate(func, (x, -1, 1)))
print(integrate(func, (x, -2, 2)))