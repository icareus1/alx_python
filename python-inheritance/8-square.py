"""
A series of classes that performs some operations
and uses the concept of inheritance
"""


class a_metaclass(type):
    """Override dir"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attri for attri in attributes if attri != '__init_subclass__']


class BaseGeometry(metaclass=a_metaclass):
    """Base Geometry class"""
    def __dir__(self) -> None:
        """
        Overrides the dir() function to exclude
        '__init_subclass__' attribute.
        """
        attributes = super().__dir__()
        return [attri for attri in attributes if attri != '__init_subclass__']

    def area(self):
        """
        Raises an exception since 'area()'
        is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the value is an integer and greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle and
    performs some operations.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
