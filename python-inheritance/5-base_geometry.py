"""Base Geometry class"""


class a_metaclass(type):
    """Override dir"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=a_metaclass):
    """Improved base geometry class""" 
    def __dir__(cls):
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")