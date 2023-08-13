"""Base Geometry class"""
class a_metaclass(type):
    """Override dir"""
    def __dir__(cls) -> None:
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class BaseGeometry(metaclass = a_metaclass):
    """"Empty base geometry class"""
    
    # def __dir__(cls) -> None:
    #     attributes = super().__dir__()
    #     return [attribute for attribute in attributes if attribute != '__init_subclass__']