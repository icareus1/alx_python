"""This module defines a simple Square class with a private attribute `size`."""
class Square:
    """This class represents a square with a private attribute `size`."""
    def __init__(self, size = 0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            print("size must be an integer")