# SELECTION SORT

def find_smallest(list_):
    smallest = list_[0]
    smallest_index = 0
    for i, e in enumerate(list_):
        if e < smallest:
            smallest = e
            smallest_index = i
    return smallest_index


def selection_sort(list_):
    sorted_list = []
    for i in range(len(list_)):
        smallest_index = find_smallest(list_)
        sorted_list.append(list_.pop(smallest_index))
    return sorted_list


selection_sort([3,7,2,4,8,0,23,3,5,8,43,86,98,43,12])

