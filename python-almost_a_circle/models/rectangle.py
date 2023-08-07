"""Rectangle module - Contains the Rectangle class"""



from models.base import Base

class Rectangle(Base):
    """Rectangle class - Inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.validate_int("width", value)
        self.validate_w_h("width", value)
        self.__width = value
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.validate_int("height", value)
        self.validate_w_h("height", value)
        self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.validate_x_y("x", value)
        self.__x = value
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.validate_x_y("y", value)
        self.__y = value
        
    def validate_int(self, name, value):
        """Check if the given value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    
    def validate_w_h(self, name, value):
        """Check if the given value is > 0."""
        if value < 1:
            raise ValueError(f"{name} must be > 0")
    
    def validate_x_y(self, name, value):
        """Check if the given value is < 0."""
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
    
    def area(self):
        """Return the area value of the rectangle"""
        return self.width * self.height
    
    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end = "")
            print("#" * self.width)
        
    def __str__(self):
        """Returns the string of Rectangle in the specified format"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args):
        attributes = ["id", "width", "height", "x", "y"]
        for i in range(min(len(args), len(self.attributes))):
            setattr(self, attributes[i], args[i])