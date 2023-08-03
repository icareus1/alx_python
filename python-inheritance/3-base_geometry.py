"""Base Geometry class"""
class BaseGeometry:
    """Empty base geometry class"""
    pass

# Override __dir__ for the class object
BaseGeometry.__dir__ = lambda: [attr for attr in BaseGeometry.__dict__ if attr != '__init_subclass__']