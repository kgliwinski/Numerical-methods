import scipy.integrate
import numpy as np

x = np.linspace(0, 3)
y = 1 - np.exp(-2*x)
res = scipy.integrate.trapezoid(y, x=x)

print(res)