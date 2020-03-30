"""Dutch National Flag Problem Given an input array consisting on only 0, 1,
and 2, sort the array in a single traversal. You're not allowed to use any
sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you
traverse the array twice, that would still be an O(n) solution but it will
not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a
    single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_idx = 0
    two_idx = len(input_list) - 1
    traversal_idx = 0

    while traversal_idx <= two_idx:
        if input_list[traversal_idx] == 0:
            if zero_idx < traversal_idx:
                # swap
                input_list[traversal_idx] = input_list[zero_idx]
                input_list[zero_idx] = 0
            else:
                traversal_idx += 1
            zero_idx += 1
        elif input_list[traversal_idx] == 2:
            if two_idx > traversal_idx:
                input_list[traversal_idx] = input_list[two_idx]
                input_list[two_idx] = 2
            else:
                traversal_idx += 1
            two_idx -= 1
        else:
            traversal_idx += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0,
               2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
test_function([1, 0, 0, 0, 0, 0, 0])
