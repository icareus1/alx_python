"""Check if object is an instance of a sub class"""
def inherits_from(obj, a_class):
    """Check if object is an instance of a sub class"""
    return isinstance(obj, type) or issubclass(type(obj), a_class)