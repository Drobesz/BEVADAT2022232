def subset(lst, i1, i2): return lst[i1:i2+i1]
def every_nth(lst, step): return [item for item in lst if lst.index(item) % step == 0]
def unique(lst): return len([item for item in lst if lst.count(item) == 1]) == len(lst)
def flatten(lst): return [item for sublist in lst for item in sublist]
def merge_lists(*args): return flatten([item for item in args])
def reverse_tuples(lst): return [item[::-1] for item in lst]
def remove_duplicates(lst): return list(set(lst))
def transpose(lst): return [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]
def split_into_chunks(lst, chunk): return [lst[i:i+chunk] for i in range(0, len(lst), chunk)]
def merge_dicts(*args): return {key: value for arg in args for key, value in arg.items()}
def by_parity(lst): return {"even":[item for item in lst if item % 2 == 0],"odd":[item for item in lst if item % 2 == 1]}
def mean_key_value(dict): return {key: sum(value)/len(value) for key, value in dict.items()}
"""
lista = [1, 1, 1, 2, 3, 4, 5, 2, 3]
print(subset([1, 2, 3], 0, 2))
print(every_nth([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
print(unique([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(flatten([[1,2],[3,4],[5,6]]))
print(merge_lists([1, 2, 3], [4, 5, 6], [7]))
print(reverse_tuples([(1,2),(3,4)]))
print(remove_duplicates([1,2,3,3,4,5]))
print(transpose([[1,2,3],
                [4,5,6],
                [7,8,9]]))
print(split_into_chunks([0, 1, 2, 3, 4, 5, 6, 7, 8], 2))
print(merge_dicts({"one":1,"two":2}, {"four":4,"three":3}))
print(by_parity([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(mean_key_value({"some_key":[1,2,3,4],"another_key":[1,2,3,4]}))
"""