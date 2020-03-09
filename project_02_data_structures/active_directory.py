"""In Windows Active Directory, a group can consist of user(s) and group(s)
themselves. We can construct this hierarchy as such. Where User is
represented by str representing their ids.


Write a function that provides an efficient look up of whether the user is
in a group.
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user == "":
        print('User cannot be empty string')
        return

    def check_user_nested_groups(user_to_verify, group_list):
        if group_list:
            group_under_test = group_list.pop()
            if user_to_verify in group_under_test.get_users():
                return True
            else:
                for element in group_under_test.get_groups():
                    group_list.add(element)
                return check_user_nested_groups(user, group_list)
        else:
            return False

    return check_user_nested_groups(user, {group})


def test_parent():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("Is sub_child_user member of Parent?")
    print(is_user_in_group('sub_child_user', parent))
    print("")

    print("Is invalid_user member of Parent?")
    print(is_user_in_group('no_child_user', parent))
    print("")


def test_child():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("Is sub_child_user member of child?")
    print(is_user_in_group('sub_child_user', child))
    print("")

    print("Is invalid_user member of child?")
    print(is_user_in_group('no_child_user', child))
    print("")


def test_sub_child():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("Is sub_child_user member of sub_child?")
    print(is_user_in_group('sub_child_user', sub_child))
    print("")

    print("Is invalid_user member of sub_child?")
    print(is_user_in_group('sub_child_user', sub_child))
    print("")


if __name__ == '__main__':
    test_parent()
    test_child()
    test_sub_child()
