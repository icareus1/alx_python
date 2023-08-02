"""Check if object is an instance of a sub class"""
def inherits_from(obj, a_class):
    """Check if object is an instance of a sub class"""
    return isinstance(obj, type) and issubclass(type(obj), a_class)