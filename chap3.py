# Chapter on Recusion and Call Stack

def my_sum(list_of_nums):
    if list_of_nums == []:
        return 0
    return list_of_nums[0] + my_sum(list_of_nums[1:])


assert my_sum([1, 2, 3, 4, 5]) == 15
assert my_sum([1, 2, 3])  == 6
assert my_sum([]) == 0
