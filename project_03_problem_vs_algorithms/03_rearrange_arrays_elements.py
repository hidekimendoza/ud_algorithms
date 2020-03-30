""" Rearrange Array Elements Rearrange Array Elements so as to form two
number such that their sum is maximum. Return these two numbers. You can
assume that all array elements are in the range [0, 9]. The number of digits
in both the numbers cannot differ by more than 1. You're not allowed to use
any sorting function that Python provides and the expected time complexity is
O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be
[542, 31]. In scenarios such as these when there are more than one possible
answers, return any one.

Here is some boilerplate code and test cases to start with:
"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        print('List must have 2 numbers to be supported')
        raise ValueError('Invalid list')

    number1 = 0
    number2 = 0
    offset = 0

    heapsort(input_list)
    while input_list:
        number_to_insert = input_list.pop()
        if (10 ** offset) > (number1 - number2):
            number1 = (number1 * 10) + number_to_insert
        else:
            number2 = (number2 * 10) + number_to_insert
            offset += 1

    return [number1, number2]


def heapify(arr, n, i):
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index)


def heapsort(arr):
    for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


try:
    rearrange_digits([])
except ValueError:
    print("Pass")
else:
    print("Fail")
test_function([[1, 0, 0], [10, 0]])
test_function([[0, 0, 0], [0, 0]])
test_function([[8, 8, 8, 8, 8, 8], [888, 888]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
