import numpy as np

eg_arr = np.random.random((3, 4))
print(eg_arr)

print(eg_arr.sum(), eg_arr.min(), eg_arr.min(axis=0), eg_arr.max(axis=1))