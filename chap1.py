# BINARY SEARCH

# def binary_search(sorted_list, elem_to_find, counter=1):
#     print(f"Counter: {counter}")
#     list_len = len(sorted_list)
#     idx_check = int(list_len / 2)
#     match sorted_list[idx_check]:
#         case elem if len(sorted_list) <= 1 and elem != elem_to_find:
#             return None
#         case elem if elem == elem_to_find:
#             return elem
#         case elem if elem > elem_to_find:
#             return binary_search(sorted_list[:idx_check], elem_to_find, counter=counter+1)
#         case elem if elem < elem_to_find:
#             return binary_search(sorted_list[idx_check:], elem_to_find, counter=counter+1)

# print(binary_search([x for x in range(1, 240000)], 90012))

def binary_search(sorted_list, elem_to_find):
    counter = 0
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        counter += 1
        print(f"Counter: {counter}")
        mid = int((low + high) / 2)
        elem = sorted_list[mid]
        if elem == elem_to_find:
            return mid
        if elem > elem_to_find:
            high = mid - 1
        if elem < elem_to_find:
            low = mid + 1
    return None

# [1,2,3,4,5]  2


print(binary_search([x for x in range(1, 258)], 1))


# https://nedbatchelder.com/text/bigo.html
