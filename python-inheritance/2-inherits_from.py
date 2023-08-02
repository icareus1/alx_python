"""Check if object is inherited from a class(directly or indirectly)"""
def inherits_from(obj, a_class):
    """Check if object is inherited from a class(directly or indirectly)"""
    return isinstance(obj, type) or issubclass(obj, a_class)