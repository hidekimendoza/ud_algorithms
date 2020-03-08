"""Union and Intersection of Two Linked Lists Your task for this problem is
to fill out the union and intersection functions. The union of two sets A and
B is the set of elements which are in A, in B, or in both A and B. The
intersection of two sets A and B, denoted by A ∩ B, is the set of all objects
that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed
of either the union or intersection, respectively. Once you have completed
the problem you will create your own test cases and perform your own run time
analysis on the code.

We have provided a code template below, you are not required to use it:"""
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    new_list = llist_1
    list_2_node = llist_2.head
    while list_2_node:
        new_list.append(list_2_node)
        list_2_node = list_2_node.next
    return new_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    new_list = LinkedList()
    second_list_head = llist_2.head
    while second_list_head:
        first_list_head = llist_1.head
        while first_list_head:
            if first_list_head.value == second_list_head.value:
                new_list.append(first_list_head.value)
                break
            first_list_head = first_list_head.next
        second_list_head = second_list_head.next
    return new_list


class TestLinkedListUnionIntersectionTest(unittest.TestCase):

    def test_union_a(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        # [4, 6, 6, 21]

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        expected_str = '3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> ' \
                       '6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> '
        self.assertEqual(union(linked_list_1, linked_list_2).__str__(),
                         expected_str)
        print(intersection(linked_list_1, linked_list_2).__str__())

    def test_intersection_a(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        # [4, 6, 6, 21]

        for i in element_1:
            linked_list_1.append(i)
        for i in element_2:
            linked_list_2.append(i)

        expected_str = '6 -> 4 -> 6 -> 21 -> '
        self.assertEqual(intersection(linked_list_1, linked_list_2).__str__(),
                         expected_str)

    def test_union_b(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        element_2 = [1, 7, 8, 9, 11, 21, 1]

        for i in element_1:
            linked_list_1.append(i)
        for i in element_2:
            linked_list_2.append(i)

        expected_str = '3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3' \
                       ' -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> '
        self.assertEqual(union(linked_list_1, linked_list_2).__str__(),
                         expected_str)
        print(intersection(linked_list_1, linked_list_2).__str__())

    def test_intersection_b(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        element_2 = [1, 7, 8, 9, 11, 21, 1]
        # ""

        for i in element_1:
            linked_list_1.append(i)
        for i in element_2:
            linked_list_2.append(i)

        expected_str = ''
        self.assertEqual(intersection(linked_list_1, linked_list_2).__str__(),
                         expected_str)


def test_with_one_empty_list():
    print('With one empty linked list')
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    print('first list: {}'.format(linked_list_1.__str__()))
    print('second list: {}'.format(linked_list_2.__str__()))

    print('union = {}'.format(union(linked_list_1, linked_list_2).__str__()))
    print('intersection = {}'.format(intersection(linked_list_1,
                                                  linked_list_2).__str__()))

    print('With one empty linked list part 2, swapping lists')
    print('union = {}'.format(union(linked_list_2, linked_list_1).__str__()))
    print('intersection = {}'.format(intersection(linked_list_2,
                                                  linked_list_1).__str__()))
    print('')


def test_with_intersection():
    print('Test with intersections')
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    # [4, 6, 6, 21]

    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    print('first list: {}'.format(linked_list_1.__str__()))
    print('second list: {}'.format(linked_list_2.__str__()))

    print('Union: {}'.format(union(linked_list_1,
                                   linked_list_2).__str__()))
    print('Intersection: {}'.format(intersection(linked_list_1,
                                                 linked_list_2).__str__()))
    print('')


def test_without_intersection():
    print('Test without intersections')
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    print('first list: {}'.format(linked_list_1.__str__()))
    print('second list: {}'.format(linked_list_2.__str__()))

    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    print('Union: {}'.format(union(linked_list_1,
                                   linked_list_2).__str__()))
    print('Intersection: {}'.format(intersection(linked_list_1,
                                                 linked_list_2).__str__()))
    print('')


if __name__ == '__main__':
    test_with_one_empty_list()
    test_with_intersection()
    test_without_intersection()
