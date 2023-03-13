import numpy as np
def column_swap(matrix):
    matrix = np.array(matrix)
    matrix[:, [0, len(matrix[0]) - 1]] = matrix[:, [len(matrix[0]) - 1, 0]]
    return matrix
def compare_two_array(matrix): return np.fill_diagonal(matrix, 1)
def get_array_shape(arr): 
    arr = np.array(arr)
    return "sor: " + (str(arr.shape[0]) or "1") + ", oszlop: " + (str(arr.shape[1]) if len(arr.shape) >= 2 else "1" if arr.shape[0] != 0 else "0") + ", melyseg: " + (str(arr.shape[2]) if len(arr.shape) >= 3 else "1" if arr.shape[0] != 0 else "0")
def encode_Y(arr, class_len): 
    output = np.zeros(len(arr) * class_len).reshape(len(arr), class_len)
    for x in arr:
        output[x, arr[x]] = 1
    return output
def decode_Y(matrix): return np.array([np.where(item == 1) for item in matrix]).reshape(-1)
def eval_classification(elem, prob): return elem[np.argmax(prob)]
def repalce_odd_numbers(lst):
    lst = np.array(lst)
    lst[lst % 2 == 1] = -1
    return lst
def replace_by_value(lst, val):
    lst = np.array(lst)
    lst[lst < val] = -1
    lst[lst >= val] = 1
    return lst
def array_multi(arr): return np.prod(arr)
def array_multi_2d(arr): return np.prod(arr, axis=1)
def add_border(arr): return np.pad(np.array(arr), 1, constant_values=(0))
def list_days(d1, d2): return np.arange(np.datetime64(d1, 'D'), np.datetime64(d2, 'D'))
def today(): return np.datetime64('today')
def sec_from_1970(): return int((np.datetime64('now') - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's'))

"""
testarray = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
testarray = np.arange(12).reshape(4, 3)
print(testarray)
print(column_swap(testarray))
print(get_array_shape(testarray))
print(encode_Y([1, 2, 0, 3], 4))
print(decode_Y(np.array([[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])))
print(eval_classification(['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]))
print(repalce_odd_numbers([1, 2, 3, 4, 5]))
print(replace_by_value([1, 2, 5, 0], 2))
print(array_multi_2d(testarray))
print(add_border([[1,2],[3,4]]))
print(list_days('2023-03', '2023-04'))
print(today())
print(sec_from_1970())
"""