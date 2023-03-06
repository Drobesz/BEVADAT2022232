def contains_odd(lst): return len([num for num in lst if num % 2]) != 0
def is_odd(lst): return list(map(lambda x: (x % 2 == 1), lst))
def element_wise_sum(lst1, lst2): return list(map(lambda x, y: (x + y), lst1, lst2))
def dict_to_list(dict): return list(map(lambda x, y: ((x, y)), dict.keys(), dict.values()))
"""
print(contains_odd([2, 4, 6]))
print(is_odd([1, 2, 3, 4, 5, 6]))
print(element_wise_sum([1, 2, 3, 4, 5, 6], [2, 4, 6]))
print(dict_to_list({"Egy":1, "Kettő":2, "Három": 3}))
"""