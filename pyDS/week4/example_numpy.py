import numpy as np

print(np.__version__)   # 1.26.4

eg_list = [[1, 2, 3], [4, 5, 5]]
eg_arr_from_list = np.array(eg_list)
print(eg_arr_from_list, eg_arr_from_list.shape, eg_arr_from_list.dtype)

eg_arr_from_method_1 = np.ones((2, 2))
eg_arr_from_method_2 = np.ones(2)
eg_arr_from_method_3 = np.identity(2)

print(eg_arr_from_method_1, eg_arr_from_method_2, eg_arr_from_method_3, sep='\n')