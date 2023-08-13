"""Base Geometry class"""



class BaseGeometry():
    """Base Geometry class"""
    
class a_metaclass(type):
    """Override dir"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
        
BaseGeometry = __import__("5-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry and perform some operations"""
    def __init__(self, width, height):
        self._height = super().integer_validator("width", width)
        self._width =  super().integer_validator("height", height)
        
    def __dir__(cls):
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']