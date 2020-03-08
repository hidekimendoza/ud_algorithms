"""A Huffman code is a type of optimal prefix code that is used for
compressing data. The Huffman encoding and decoding schema is also lossless,
meaning that when compressing the data to make it smaller, there is no loss
of information.

The Huffman algorithm works by assigning codes that correspond to the
relative frequency of each character for each character. The Huffman code can
be of any length and does not require a prefix; therefore, this binary code
can be visualized on a binary tree with each encoded character being stored
on leafs.

There are many types of pseudocode for this algorithm. At the basic core,
it is comprised of building a Huffman tree, encoding the data, and, lastly,
decoding the data.

Here is one type of pseudocode for this coding schema:

Take a string and determine the relevant frequencies of the characters. Build
and sort a list of tuples from lowest to highest frequencies. Build the
Huffman Tree by assigning a binary code to each letter, using shorter codes
for the more frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built
tree). Encode the text into its compressed form. Decode the text from its
compressed form. """

import unittest
from collections import defaultdict
from queue import PriorityQueue


class Node:
    def __init__(self, value, hier):
        self.value = value
        self.hier = hier
        self.left_node = None
        self.right_node = None

    def has_childs(self):
        return bool(self.right_node or self.left_node)

    def __lt__(self, other):
        if self.hier == other.hier:
            if self.has_childs() and not other.has_childs():
                return False
            elif not self.has_childs() and other.has_childs():
                return True
            else:
                return True
        return self.hier < other.hier


def get_different_chars_with_count(data):
    characters = defaultdict(lambda: 0)
    for character in data:
        characters[character] += 1
    return characters


def sort_data(data):
    sorted_data = PriorityQueue()
    keys = set()
    for key, val in get_different_chars_with_count(data).items():
        sorted_data.put(Node(key, val))
        keys.add(key)
    return sorted_data, keys


def huffman_encoding(data):
    if not data:
        return '', None
    tree, keys = sort_data(data)

    while tree.qsize() > 1:
        node_left = tree.get()
        node_right = tree.get()
        new_node = Node(None, node_left.hier + node_right.hier)
        new_node.left_node = node_left
        new_node.right_node = node_right
        tree.put(new_node)

    # If is possible to get last element of PriorityQueue without removing it?
    new_tree = tree.get()

    codes = dict()
    for key in keys:
        codes[key] = ''.join(path_from_root_to_node(new_tree, key)[1:])

    encoded_data = ''
    for char in data:
        encoded_data += codes[char]

    return encoded_data, new_tree


def path_from_root_to_node(root, data):
    if root is None:
        return None

    elif root.value == data:
        return [data]

    left_answer = path_from_root_to_node(root.left_node, data)
    if left_answer is not None:
        left_answer.insert(1, '0')
        return left_answer

    right_answer = path_from_root_to_node(root.right_node, data)
    if right_answer is not None:
        right_answer.insert(1, '1')
        return right_answer
    return None


def huffman_decoding(data, tree):
    decoded_str = ''
    while len(data):
        try:
            decoded_char, data = get_decoded_char(data, tree)
        except IndexError:
            print('Invalid input into Huffman decoder')
            return ''
        decoded_str += decoded_char
    return decoded_str


def get_decoded_char(encoded_str, root):
    if not root.has_childs():
        return root.value, encoded_str
    else:
        if encoded_str[0] == '0':
            return get_decoded_char(encoded_str[1:], root.left_node)
        else:
            return get_decoded_char(encoded_str[1:], root.right_node)


class TestHuffmanEncoding(unittest.TestCase):
    def test_get_different_chars_with_count(self):
        input_str = 'The bird is the word'
        expected = {'T': 1, 'h': 2, 'e': 2, ' ': 4, 'b': 1, 'i': 2, 'r': 2,
                    'd': 2, 's': 1, 't': 1, 'w': 1, 'o': 1}
        self.assertEqual(get_different_chars_with_count(input_str), expected)

    def test_sort_data_len(self):
        input_str = 'The bird is the word'
        sorted_queue, keys = sort_data(input_str)
        self.assertEqual(sorted_queue.qsize(), 12)
        self.assertEqual(keys, {'T', 'b', 'o', 's', 't', 'w', 'd', 'e', 'h',
                                'i', 'r', ' '})

        # (1, 'T')
        # (1, 'b')
        # (1, 'o')
        # (1, 's')
        # (1, 't')
        # (1, 'w')
        # (2, 'd')
        # (2, 'e')
        # (2, 'h')
        # (2, 'i')
        # (2, 'r')
        # (4, ' ')

    def test_path_to_root(self):
        root = Node(None, 20)
        root.left_node = Node(None, 8)
        root.right_node = Node(None, 12)
        root.left_node.left_node = Node(' ', 4)
        root.left_node.right_node = Node(None, 4)
        root.left_node.right_node.left_node = Node('h', 2)
        root.left_node.right_node.right_node = Node('r', 2)

        self.assertEqual(path_from_root_to_node(root, ' '), [' ', '0', '0'])
        self.assertEqual(path_from_root_to_node(root, 'h'),
                         ['h', '0', '1', '0'])
        self.assertEqual(path_from_root_to_node(root, 'r'),
                         ['r', '0', '1', '1'])

    def test_create_tree(self):
        input_str = 'The bird is the word'
        data, _ = huffman_encoding(input_str)
        expected = '111110101100001111010001111010010' \
                   '0101000111010101100001011111000111101'
        self.assertEqual(expected, data)

    def test_get_decoded_char(self):
        input_str = 'The bird is the word'
        _, tree = huffman_encoding(input_str)
        codes = {'T': '11111', 'w': '1011', 'o': '11100', 'r': '011',
                 's': '1010', 'e': '1100', 'h': '010', 'b': '11110',
                 'd': '1101', 't': '11101', ' ': '00', 'i': '100'}

        for key, value in codes.items():
            self.assertEqual(get_decoded_char(value, tree), (key, ''))

    def test_decoded_huffman_decoding(self):
        a_great_sentence = "The bird is the word"

        encoded_data, tree = huffman_encoding(a_great_sentence)
        self.assertEqual(a_great_sentence, huffman_decoding(encoded_data, tree))


def test_empty():
    print('Encoding, decoding empty string')
    encoded_data, tree = huffman_encoding('')
    print('Encoded output: \'{}\''.format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print('decoded output: \'{}\''.format(decoded_data))
    print('')


def test_with_string():
    input_str = 'The bird is the word'
    print('Encoding, decoding string: \'{}\''.format(input_str))
    encoded_data, tree = huffman_encoding(input_str)
    print('Encoded output: \'{}\''.format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print('decoded output: \'{}\''.format(decoded_data))
    print('')


def test_with_invalid_decode():
    input_str = 'The bird is the word'
    print('Encoding, decoding string: \'{}\''.format(input_str))
    encoded_data, tree = huffman_encoding(input_str)
    print('Encoded output: \'{}\''.format(encoded_data))
    print('Change output to:'
          ' \'111110101100001111010001111\''.format(encoded_data))
    decoded_data = huffman_decoding('111110101100001111010001111', tree)
    print('decoded output: \'{}\''.format(decoded_data))
    print('')


if __name__ == '__main__':
    test_empty()
    test_with_string()
    test_with_invalid_decode()
