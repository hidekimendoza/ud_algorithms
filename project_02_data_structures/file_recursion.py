""" For this problem, the goal is to write code for finding all files under a
directory (and all directories beneath it) that end with ".c """
from os import listdir, path, getcwd

MODULE_PATH = path.dirname(__file__)
TEST_DIR = path.join(getcwd(), 'testdir')


def print_recursive_c_files(test_dir):
    try:
        dir_content = listdir(test_dir)
        for content in dir_content:
            content_path = path.join(test_dir, content)
            if path.isdir(content_path):
                print_recursive_c_files(content_path)
            else:
                if path.isfile(content_path) and is_c_file(content):
                    print(content_path)
    except FileNotFoundError:
        print('Invalid input directory')




def is_c_file(file):
    return file.endswith(".c")


def test_testdir():
    print('Get C files from {}'.format(TEST_DIR))
    print_recursive_c_files(TEST_DIR)
    print('')


def test_testdir_no_files():
    print('Get C files from {}'.format(path.join(TEST_DIR, 'subdir2')))
    print_recursive_c_files(path.join(TEST_DIR, 'subdir2'))
    print('')


def test_testdir_with_file():
    print('Get C files from {}'.format(path.join(TEST_DIR, 'subdir1')))
    print_recursive_c_files(path.join(TEST_DIR, 'subdir1'))
    print('')

def test_testdir_with_invalid_dir():
    print('Get C files from {}'.format(path.join('/invalid', 'subdir1')))
    print_recursive_c_files(path.join('/invalid', 'subdir1'))
    print('')

def test_testdir_with_file_path():
    print('Get C files from {}'.format(path.join(TEST_DIR, 'subdir1', 'a.c')))
    print_recursive_c_files(path.join(TEST_DIR, 'subdir1'))
    print('')


if __name__ == '__main__':
    test_testdir()
    test_testdir_no_files()
    test_testdir_with_file()
    test_testdir_with_invalid_dir()
    test_testdir_with_file_path()
