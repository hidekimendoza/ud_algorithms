"""Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's
runtime complexity must be in the order of O(log n).

Example:


Analysis
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

    # 4, 5, 6, 7, 8, 1, 2, 3
    # A)3 ordered             4... 6, 7, 8 ...3
    ## smaller can be:
    #    a) right if val < 3
    #    b) left if val > 3
    ## greater can be:
    #    a) right

    # B)break order at next   4... 7, 8, 1 ...3
    ## smaller can be:
    #    a) left if val > 3
    #    b) right if val < 3
    ## greater can be:
    #    none

    # C) break order at prev   4... 8, 1, 2 ...3
    ## smaller can be:
    #    none
    ## greater can be:
    #  right if < 3
    #  left if > 4
"""


def rotated_array_search(input_list):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Start at the middle
    if len(input_list[0]) == 0:
        return -1
    return get_element(input_list[0], input_list[1], 0, len(input_list[0]) - 1)


def get_element(arr, number, start_idx, end_idx):
    pivot = start_idx + ((end_idx - start_idx) // 2)
    if arr[pivot] == number:
        return pivot
    if start_idx == end_idx:
        return -1

    if number > arr[pivot]:
        if arr[start_idx] > arr[end_idx] and arr[pivot] < arr[end_idx] < number:
            return get_element(arr, number, start_idx, pivot - 1)
        return get_element(arr, number, pivot + 1, end_idx)
    else:
        if arr[start_idx] > arr[end_idx] >= number:
            if arr[pivot] > arr[end_idx]:
                return get_element(arr, number, pivot + 1, end_idx)
        return get_element(arr, number, start_idx, pivot - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_function([[], 6])

test_function([[1], 6])
test_function([[6], 6])

test_function([[2, 1], 1])
test_function([[2, 1], 3])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 0])
test_function([[6, 7, 8, 9, 10, 1], 8])

test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[10, 1, 2, 3, 4], 1])
