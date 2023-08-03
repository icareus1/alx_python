"""Base Geometry class"""
class BaseGeometry:
    """"Improved base geometry class"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    
    def area(self):
        raise Exception("area() is not implemented")