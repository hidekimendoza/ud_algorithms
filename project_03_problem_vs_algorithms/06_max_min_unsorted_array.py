"""Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of
unsorted integers. The code should run in O(n) time. Do not use Python's
inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        raise ValueError('Unable to get min and max values from empty list')

    min_value = ints[0]
    max_value = ints[0]

    for number in ints:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number

    return float(min_value), float(max_value)


def test_case_random_0_9():
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


def test_case_empty_array():
    try:
        get_min_max([])
    except ValueError:
        print 'Pass'
    else:
        print 'Fail'


def test_case_with_1_number():
    values = [1]
    print ("Pass" if ((1, 1) == get_min_max(values)) else "Fail")


def test_case_with_duplicate_number():
    values = [4, 5, 4, 4]
    print ("Pass" if ((4, 5) == get_min_max(values)) else "Fail")


if __name__ == '__main__':
    test_case_random_0_9()
    test_case_with_1_number()
    test_case_empty_array()
    test_case_with_duplicate_number()
