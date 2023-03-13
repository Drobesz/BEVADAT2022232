import numpy as np
def create_array(tpl = (2, 2)): return np.zeros(np.prod(tpl)).reshape(tpl)
def set_one(lst): return np.fill_diagonal(np.array(lst), 1)
def do_transpose(arr): return np.transpose(np.array(arr))
def round_array(arr, n = 2): return np.round(np.array(arr), decimals=n)
def bool_array(lst): 
    lst = np.array(lst)
    lst[lst == 1] = True
    lst[lst == 0] = False
    return lst
def invert_bool_array(lst):
    lst = np.array(lst)
    lst[lst == 1] = False
    lst[lst == 0] = True
    return lst
def flatten(arr): return np.array(arr).reshape(-1)

"""
print(create_array((2, 3, 4)))
print(round_array([0.1223, 0.1675, 0.9739], n = 2))
"""