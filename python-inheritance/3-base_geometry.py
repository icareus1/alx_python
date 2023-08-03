"""Base Geometry class"""
class BaseGeometry:
    """"Empty base geometry class"""
    # def __dir__(cls) -> None:
    #     return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']def __dir__(self):
    def __dir__(cls)->None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']