import numpy as np

eg_list = [[1, 2, 3], [4, 5, 6]]
eg_arr_1 = np.array(eg_list)
eg_arr_2 = np.ones((2, 3))

print(eg_arr_1 + eg_arr_2)  # int + float이어서 float으로 결과 저장됨
print(eg_arr_1 + 2)

print(np.add.reduce(eg_arr_1))
print(np.add.reduce(eg_arr_1, axis=1))
print(np.add.accumulate(eg_arr_1))