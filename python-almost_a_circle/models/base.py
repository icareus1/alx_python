"""
The `Base` class is the base class for all other classes in this project.
It manages the `id` attribute for all its subclasses and avoids code duplication.
"""



class Base:
    """Create a `Base` class that manages automatic id generation"""
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects