import scipy.linalg
import numpy as np

a = np.array([[8, 2, 1],[3, 7, 2],[2, 3, 9]])
p, l, u = scipy.linalg.lu(a)

print(p)