
# Shape is a Super class of Circle and Rectangle.
class Shape():
    def __init__(self, color = "black"):
        self.color = color
    
    def area(self):
        return NotImplementedError("Subclass must implement this method")
    
    def printMe(self):
        print(f"Color: {self.color},  and Area: {self.area()}")


## Base Classes        
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius**2
    
class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    
# Objects

circle = Circle(5, "red")
circle.printMe()

rect = Rectangle(10, 20, "blue")
rect.printMe()