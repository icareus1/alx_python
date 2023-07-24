#!/usr/bin/python3

if __name__ == "__main__":
    """Print 1 + 2 = 3 Literally by importing a module"""
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
