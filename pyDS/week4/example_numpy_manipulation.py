import numpy as np

eg_list = [[1, 2, 3], [4, 5, 6]]
eg_arr_1 = np.array(eg_list)
print(eg_arr_1.ndim, eg_arr_1.shape, eg_arr_1.size, eg_arr_1.dtype)

eg_arr_1[0, 0] = 99
eg_arr_2 = eg_arr_1[1:2, :]
eg_arr_3 = eg_arr_1.reshape(3, -1)

print(eg_arr_1, eg_arr_2, eg_arr_3, sep='\n')

print(np.vstack([eg_arr_1, eg_arr_2]))
print(np.split(eg_arr_1, [1]))