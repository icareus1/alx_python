"""Base Geometry class"""

class myclass:
    """remove init_subclass from the list of attributes and methods returned"""
    def __dir__(cls) -> None:
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']

class BaseGeometry:
    """"Empty base geometry class"""
    pass
