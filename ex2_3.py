from sympy import *


def quadratic_roots(a, b, c):
    x = symbols('x')
    f = a*x**2 + b*x+c
    print(solve(f, x))


quadratic_roots(1, 6, 2)
quadratic_roots(0, -4, 1.6)
quadratic_roots(3, 2.5, 7)
