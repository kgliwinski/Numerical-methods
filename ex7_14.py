import numpy as np
from sympy import solve, symbols

x = symbols('x')
sol = solve((x+2)*(x+5)*(x-6)*(x-4)*(x-8), x)
print(sol)