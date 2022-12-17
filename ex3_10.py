import numpy as np
import math

def cos_maclaurin(n : int, x : float) -> float:
    res = 1.0
    for i in range(n):
        k = i+1
        # print(k, k%2, math.pow(-1, k % 2))
        res += math.pow(-1, k % 2) * pow(x, 2*k) / math.factorial(2*k)
    return res

x = 1.
n = 16
print('cos(x) calculated with numpy: %f, cos(x) calculated with maclaurin in %d order: %f' %(np.cos(x), n, cos_maclaurin(n, x)))
