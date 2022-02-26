# QUICKSORT
from random import randint as r


def return_largest(arr):  # Recursive return largest
    if len(arr) == 1:
        return arr[0]
    elif arr[0] > return_largest(arr[1:]):
        return arr[0]
    return return_largest(arr[1:])


return_largest([10,11,12,54,4,5,7])
return_largest([10,11,12])
return_largest([4,-50,7])

def quicksort(arr):
    counter += 1
    arr = arr[:]
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(int(len(arr) / 2))
        less_than = [x for x in arr if x <= pivot]
        more_than = [x for x in arr if x > pivot]
        return quicksort(less_than) + [pivot] + quicksort(more_than)


rand_list = [r(-20, 60) for _ in range(6)]
qs = quicksort(rand_list)
assert qs == sorted(rand_list)
assert len(qs) == len(rand_list)
