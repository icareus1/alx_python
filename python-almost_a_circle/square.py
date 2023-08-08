"""Square module - Contains the Square class"""



from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class - Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Getter for size attribute (same as width/height in Rectangle)"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter for size attribute (same as width/height in Rectangle)"""
        self.width = value
        self.height = value
        
    def __str__(self):
        """String representation of Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"