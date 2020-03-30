"""Find the square root of the integer without using any Python library. You
have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196
whose floor value is 5.

The expected time complexity is O(log(n))
"""


def sqrt(number):
    """
    Calculate the floored square root of a numb

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    def get_sqrt(numb, possible_sqrt):
        if possible_sqrt * possible_sqrt == numb:
            return possible_sqrt
        else:
            next_sqrt = (possible_sqrt + 1) * (possible_sqrt + 1)
            if next_sqrt > numb:
                return possible_sqrt
        return get_sqrt(numb, possible_sqrt + 1)

    return get_sqrt(number, 0)


print ("Pass" if (3 == sqrt(9)) else "Fail")
print ("Pass" if (0 == sqrt(0)) else "Fail")
print ("Pass" if (4 == sqrt(16)) else "Fail")
print ("Pass" if (1 == sqrt(1)) else "Fail")
print ("Pass" if (5 == sqrt(27)) else "Fail")
