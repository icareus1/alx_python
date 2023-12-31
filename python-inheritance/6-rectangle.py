"""Base Geometry class"""



BaseGeometry = __import__("5-base_geometry").BaseGeometry

# class a_metaclass(type):
#     """Override dir"""
#     def __dir__(cls):
#         return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

# class BaseGeometry(metaclass=a_metaclass):
#     """Improved base geometry class""" 
#     def __dir__(cls):
#         attributes = super().__dir__()
#         return [attribute for attribute in attributes if attribute != '__init_subclass__']

    
#     def area(self):
#         raise Exception("area() is not implemented")
    
#     def integer_validator(self, name, value):
#         if not isinstance(value, int):
#             raise TypeError(f"{name} must be an integer")
#         if value <= 0:
#             raise ValueError(f"{name} must be greater than 0")
        


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry and perform some operations"""
    def __init__(self, width, height):
        self.__height = super().integer_validator("width", width)
        self.__width =  super().integer_validator("height", height)