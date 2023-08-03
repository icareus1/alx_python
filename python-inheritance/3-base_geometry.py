"""Base Geometry class"""
class BaseGeometry:
    """Empty base geometry class"""
    def __dir__(self):
        return [attr for attr in self.__dict__ if attr != '__init_subclass__']