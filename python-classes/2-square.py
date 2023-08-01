"""This module defines a simple Square class with a private attribute `size` and calculate its area."""
class Square:
    """This class represents a square with a private attribute `size`."""
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return self.__size ** 2