from sympy import symbols, maximum, Interval, pi
import numpy as np
x = symbols('x')

y = np.linspace(-10., 10., num=100)
func = 2.25 * x * y + 1.75 * y - 1.5 * x**2 - 2 * y**2

max = -1000.
for fs in func:
    iter = maximum(fs, x, Interval(-10, 10))
    # print(iter)
    if iter > max:
        max = iter

print(max)
