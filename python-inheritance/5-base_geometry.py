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