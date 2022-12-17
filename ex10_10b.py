import numpy as np
from scipy.linalg import lu
# program to find solutions to systems of linear systems

a = np.array([[8., 2., 1.], [3., 7., 2.], [2., 3., 9.]])
# lu function from scipy.linalg does the lu decomposition automatically
pl, u = lu(a, permute_l=True)

print(u)
