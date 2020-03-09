"""A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the
other blocks in the chain. Each block contains a cryptographic hash of the
previous block, a timestamp, and transaction data. For our blockchain we will
be using a SHA-256 hash, the Greenwich Mean Time when the block was created,
and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain
implementation.

Finally you need to link all of this together in a block chain, which you
will be doing by implementing it in a linked list. All of this will help you
build up to a simple but full blockchain implementation! """

import hashlib
from time import gmtime, strftime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode(
            'utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.tail = None
        self.size = 0
        self.head = None

    def add(self, data):
        if not self.tail:
            self.tail = Block(strftime("%Y-%m-%d %H:%M:%S",
                                       gmtime()),
                              data, None)
            self.head = self.tail
        else:
            new_block = Block(strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                              data, self.head)
            self.head = new_block
        self.size += 1

    def __str__(self):
        last_block = self.head
        string = ''
        while last_block:
            string += 'Block: \n' \
                      'block_information: \n' \
                      'timestamp: {}\n' \
                      'data: {}\n' \
                      'prev hash: {}\n' \
                      'hash: {}\n'.format(last_block.timestamp, last_block.data,
                                          last_block.previous_hash,
                                          last_block.hash)
            last_block = last_block.previous_hash
        return string


def test_empty_block_chain():
    chain = Blockchain()
    print('Empty blockchain nodes:')
    print('---')
    print(chain.__str__())
    print('---')


def test_block_chain_one_node():
    chain = Blockchain()
    chain.add('First node')
    print('Blockchain with one node:')
    print('---')
    print(chain.__str__())
    print('---')


def test_block_chain_two_nodes():
    chain = Blockchain()
    chain.add('First node')
    chain.add('Second node')
    print('Blockchain with two nodes:')
    print('---')
    print(chain.__str__())
    print('---')


if __name__ == '__main__':
    test_empty_block_chain()
    test_block_chain_one_node()
    test_block_chain_two_nodes()
