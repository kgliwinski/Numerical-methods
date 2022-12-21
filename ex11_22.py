import numpy as np
import scipy.linalg

A = np.array([[0, -7, 5], [0, 4, 7], [-4, 3, -7]])
B = np.array([50, -30, 40])

x = scipy.linalg.solve(A, B)
print(x)
print('Original:\n', A, '\nTransposed:\n', np.transpose(A))
print('Determinant:', int(np.linalg.det(A)))