import scipy.integrate
import numpy as np

x = np.linspace(0, 0.8)
y = 0.2 + 25*x - 200 * x **2 + 675 * x**3 - 900 * x**4 + 400 * x**5
res = scipy.integrate.simpson(y, x=x)

print(res)