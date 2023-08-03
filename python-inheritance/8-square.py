"""Base Geometry class"""



class BaseGeometry:
    """"Improved base geometry class"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry and performs some operations"""
    
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        return self.__width * self.__height
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
class Square(Rectangle):
    """A class Square that inherits from Rectangle and performs some operations"""
    
    
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
    def __str__(self):
        return f"[Square] {self.__width}/{self.__height}"
