#!/usr/bin/python3

"""Custome Classes"""


class MyList(list):
    """A variant of list class"""


    def print_sorted(self):
        """prints MyList in sorted form"""
        print(sorted(self))


if __name__ == '__main__':
    a = MyList()
    a.append(6)
    a.append(3)
    a.append(4)
    a.append(13)
    print(a)
    a.print_sorted()
