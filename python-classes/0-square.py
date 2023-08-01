"""
Square Class

This module defines a simple Square class with a private attribute `size`.

Attributes:
    size (int): The size of the square's sides (private).

Methods:
    __init__(self, size): Initializes a new Square instance with the given size.
"""
class Square:
    def __init__(self, size):
        self.__size = size