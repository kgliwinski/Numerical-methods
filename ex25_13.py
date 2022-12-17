import numpy as np
import math

def runge_kutta_4(h: float, x: float, x0: float, y0: float, diff) -> float:
    # step size n
    n = (int)((x-x0) / h)
    # print(n)
    y = y0
    # iterate n times
    for i in range(n):
        k1 = h * diff(x0, y)
        k2 = h * diff(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * diff(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * diff(x0 + h, y + k3)

        # Update value of y
        y = y + (1.0/6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        # Update value of x0
        x0 = x0 + h

    # dif_eq.y = y
    return y


def dydx1(x, y):
    return -2*x ** 3 + 12*x ** 2 - 20 * x + 8.5


def dydx2(x, y) -> float:
    p = 0.8 * x
    4. * math.pow(2.71, p) - 0.5*y


H = 0.5
# print(dydx2(1.0, 2.0))
a = runge_kutta_4(H, 0.5, 0., 1., dydx1)
print(a)

# b = runge_kutta_4(H, 0.5, 0., 2., dydx2)
