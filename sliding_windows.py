
def find_averages_of_subarrays(k_window_size, arr):
    """Given an array, find the average of all subarrays of
    'k' contiguous elements in it."""
    window_sum, window_start, result = 0.0, 0, []
    for window_end, elem in enumerate(arr, 1):
        window_sum += elem
        if window_end >= k_window_size:
            window_avg = window_sum / k_window_size
            result.append(window_avg)
            window_sum -= arr[window_start]
            window_start += 1
    return result


assert find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]


def find_max_sum_subarrays(k_window_size, arr):
    """Given an array of positive numbers and a positive number 'k'
    find the maximum sum of any contiguous subarray of size 'k'"""
    window_sum, window_start, max_sum = 0.0, 0, 0
    for window_end, elem in enumerate(arr, 1):
        window_sum += elem
        if window_end >= k_window_size:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


assert find_max_sum_subarrays(3, [2, 1, 5, 1, 3, 2]) == 9
assert find_max_sum_subarrays(2, [2, 3, 4, 1, 5]) == 7


def find_max_len_subarray_above_or_equal_num(s, arr):
    """Given an array of positive numbers and a positive number
    'S', find the length of the smallest contiguous subarray
    whose sum is greater than or equal to 'S'. Return 0 if no
    such subarray exists."""
    window_start, window_sum, smallest_window = 0, 0, len(arr)
    for window_end, elem in enumerate(arr):
        window_sum += elem
        while window_sum >= s:
            smallest_window = min(smallest_window, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    return smallest_window


assert find_max_len_subarray_above_or_equal_num(7, [2, 1, 5, 2, 3, 2]) == 2
assert find_max_len_subarray_above_or_equal_num(7, [2, 1, 5, 2, 8]) == 1
assert find_max_len_subarray_above_or_equal_num(10, [2, 1, 5, 2, 3, 2]) == 3
assert find_max_len_subarray_above_or_equal_num(8, [3, 4, 1, 1, 6]) == 3


