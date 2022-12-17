import numpy as np


class diff:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    pass
# program to solve differential equations using
# 4th order runge-kutta method


def runge_kutta_4(h: float, dif_eq: diff, dif_eq0: diff) -> float:
    # step size n
    x = dif_eq.x
    x0 = dif_eq0.x
    y0 = dif_eq0.y
    n = (x-x0)//h
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


STEP = 0.5
f1 = diff(0, -0.5)
for x in range(0., 5., STEP):

    f1_0 = diff(x, -0.5*x)
    y1 = runge_kutta_4(STEP, f1, f1_0)
    f2 = diff(0, 4 + 0.3*x - 0.1*y1)
    y2 = runge_kutta_4(STEP, )
