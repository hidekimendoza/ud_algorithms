"""
We have briefly discussed caching as part of a practice problem while
studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed
to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache,
it is known as a cache hit. If, however, the entry is not found,
it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the
cache. If the cache is full and we want to add a new entry to the cache,
we use some criteria to remove an element. After removing an element, we use
the put() operation to insert the new element. The remove operation should
also be fast.

For our first problem, the goal will be to design a data structure known as a
Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we
remove the least recently used entry when the cache memory reaches its limit.
For the current problem, consider both get and set operations as an use
operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate
value. In case of a cache miss, your get() should return -1. While putting an
element in the cache, your put() / set() operation must insert the element.
If the cache is full, you must write code that removes the least recently
used entry first and then insert the element. All operations must take O(1)
time.

For the current problem, you can consider the size of cache = 5
"""
import unittest


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, size):
        self.head = None  # Oldest
        self.tail = None  # Newest
        self.num_elements = 0
        self.size = size
        self.addresses = {}  # key - node dictionary

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if not self.addresses.get(key):
            new_node = Node(key, value)
            self.addresses[key] = new_node
            if self.head is None:  # Empty queue
                self.head = new_node
                self.tail = self.head
                self.num_elements += 1
            else:
                if self.num_elements < self.size:  # Not full queue
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = self.tail.next
                    self.num_elements += 1
                else:  # Full queue
                    # remove old node
                    to_remove = self.head.key
                    self.head = self.head.next
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = self.tail.next
                    del self.addresses[to_remove]
        else:
            self.addresses[key].value = value
            self._move_to_tail(self.addresses[key])

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.addresses:
            # Cache hit
            self._move_to_tail(self.addresses[key])
            return self.addresses[key].value
        else:
            # Cache miss
            return -1

    def _move_to_tail(self, node):  # Cache hit
        if node == self.head:
            self.head = self.head.next
        else:
            node.prev.next = node.next
        if self.num_elements > 1:
            node.next.prev = node.prev
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def __str__(self):
        data = self.head
        out_str = ''
        while data:
            out_str += '{} -> '.format(data.value)
            data = data.next
        out_str += 'x'
        return out_str


class TestLRU(unittest.TestCase):
    def test_lru_creation(self):
        """ lru shall create structure with length capacity """
        our_cache = LRUCache(5)
        self.assertEqual(our_cache.num_elements, 0)
        self.assertEqual(our_cache.size, 5)

    def test_lru_add_data_till_overflow(self):
        """ Set the value of one item is the key is not present """
        our_cache = LRUCache(5)
        our_cache.set(1, 1)
        self.assertEqual(our_cache.tail.key, 1)
        self.assertEqual(our_cache.tail.value, 1)
        our_cache.set(2, 2)
        self.assertEqual(our_cache.tail.key, 2)
        self.assertEqual(our_cache.tail.value, 2)
        self.assertEqual(our_cache.head.key, 1)
        self.assertEqual(our_cache.head.value, 1)
        our_cache.set(3, 3)
        self.assertEqual(our_cache.tail.key, 3)
        self.assertEqual(our_cache.tail.value, 3)
        our_cache.set(4, 4)
        self.assertEqual(our_cache.tail.key, 4)
        self.assertEqual(our_cache.tail.value, 4)
        our_cache.set(5, 5)
        self.assertEqual(our_cache.tail.key, 5)
        self.assertEqual(our_cache.tail.value, 5)
        self.assertEqual(our_cache.head.key, 1)
        self.assertEqual(our_cache.head.value, 1)
        our_cache.set(6, 6)
        self.assertEqual(our_cache.tail.key, 6)
        self.assertEqual(our_cache.tail.value, 6)
        self.assertEqual(our_cache.head.key, 2)
        self.assertEqual(our_cache.head.value, 2)

    def test_lru_add_data_cache_hit(self):
        our_cache = LRUCache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(1, 3)
        self.assertEqual(our_cache.num_elements, 2)
        self.assertEqual(our_cache.tail.key, 1)
        self.assertEqual(our_cache.tail.value, 3)
        self.assertEqual(our_cache.head.key, 2)
        self.assertEqual(our_cache.head.value, 2)

    def test_lru_get_data_if_not_data(self):
        our_cache = LRUCache(5)
        self.assertEqual(our_cache.get(1), -1)
        our_cache.set(1, 1)

    def test_lru_get_data_complete_flow(self):
        our_cache = LRUCache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)
        self.assertEqual(our_cache.get(1), 1)
        self.assertEqual(our_cache.get(2), 2)
        self.assertEqual(our_cache.get(9), -1)
        our_cache.set(5, 5)
        our_cache.set(6, 6)
        self.assertEqual(our_cache.get(3), -1)


def test_a_overflow_cache():
    print('Inserting to cache numbers until overflow')
    our_cache = LRUCache(5)
    for i in range(5):
        our_cache.set(i, i)
    print('Cache before overflow: {}'.format(our_cache.__str__()))
    print('Addresses: {}'.format(our_cache.addresses.keys()))
    our_cache.set(9, 9)
    print('Cache after overflow: {}'.format(our_cache.__str__()))
    print('Addresses: {}'.format(our_cache.addresses.keys()))
    print()


def test_b_complete_flow():
    print('Inserting to cache gets')
    our_cache = LRUCache(5)
    for i in range(5):
        our_cache.set(i, i)
    print('Cache: {}'.format(our_cache.__str__()))
    print('Addresses: {}'.format(our_cache.addresses.keys()))

    print('Try to get \'1\', result = {}'.format(our_cache.get(1)))
    print('Try to get \'2\', result = {}'.format(our_cache.get(2)))
    print('Try to get \'9\', result = {}'.format(our_cache.get(9)))

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print('Cache after add 5 and 6: {}'.format(our_cache.__str__()))
    print('Addresses: {}'.format(our_cache.addresses.keys()))
    print('Try to get \'3\', result = {}'.format(our_cache.get(3)))
    print('')


def test_c_get_from_empty_cache_and_write_first_element():
    our_cache = LRUCache(5)
    print('Get value from empty cache')
    print('Cache: {}'.format(our_cache.__str__()))
    print('Addresses: {}'.format(our_cache.addresses.keys()))
    print('Try to get \'1\', result = {}'.format(our_cache.get(1)))
    print('Set first value')
    our_cache.set(1, 1)
    print('Cache: {}'.format(our_cache.__str__()))
    print('Addresses: {}'.format(our_cache.addresses.keys()))
    print('Try to get \'1\', result = {}'.format(our_cache.get(1)))


if __name__ == '__main__':
    test_a_overflow_cache()
    test_b_complete_flow()
    test_c_get_from_empty_cache_and_write_first_element()
