"""Check if object is inherited from a class(directly or indirectly)"""


def inherits_from(obj, a_class):
    """Check if object is inherited from a class(directly or indirectly)"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
