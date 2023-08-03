""""A series of classes that performs some operations and uses the concept of inheritance"""
class BaseGeometry:
    """Base Geometry class"""

    def __dir__(self) -> None:
        """Overrides the dir() function to exclude '__init_subclass__' attribute."""
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

    def area(self):
        """Raises an exception since 'area()' is not implemented in the base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the value is an integer and greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry and performs some operations."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class Square that inherits from Rectangle and performs some operations."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
