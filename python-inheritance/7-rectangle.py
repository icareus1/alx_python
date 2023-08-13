"""Base Geometry class"""



# class a_metaclass(type):
#     """Override dir"""
#     def __dir__(cls) -> None:
#         return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
# class BaseGeometry(metaclass = a_metaclass):
#     """Improved base geometry class""" 
#     def __dir__(cls) -> None:
#         attributes = super().__dir__()
#         return [attribute for attribute in attributes if attribute != '__init_subclass__']
    
#     def area(self):
#         raise Exception("area() is not implemented")
    
#     def integer_validator(self, name, value):
#         if not isinstance(value, int):
#             raise TypeError(f"{name} must be an integer")
#         if value <= 0:
#             raise ValueError(f"{name} must be greater than 0")

BaseGeometry = __import__("5-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry and perform some operations"""
    def __init__(self, width, height):
        self.__height = super().integer_validator("width", width)
        self.__width =  super().integer_validator("height", height)
    
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"