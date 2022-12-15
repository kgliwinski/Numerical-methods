import numpy as np
# Ex. 7.4 - simple polynomial roots calculation

# Representation of the x^3 - x^2 + 2x - 2 = (x^2 + 2)(x-1) from
# example (a), and so on
p_a = np.array([1, -1, 2, -2])
p_b = np.array([2, 0, 6, 0, 8])
p_c = np.array([1, -2, 6, -2, 5])

# printing the roots of each polynomial
print('a):', np.roots(p_a))
print('b):', np.roots(p_b))
print('c):', np.roots(p_c))
