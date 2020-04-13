class Polygon(object):
    """Base class"""
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def perimeter(self):
        return 0
    def area(self):
        return 0

class Rectangle(Polygon):
    """Derived class"""
    def __init__(self, name, side1 = 10, side2 = 10):
        super(Rectangle, self).__init__(name)
        self.side1 = side1
        self.side2 = side2
    def perimeter(self):
        return (self.side1 + self.side2) * 2
    def area(self):
        return self.side1 * self.side2

# class example with inheritance and polymorphism
polygon = Rectangle("my figure", 2, 5)
print("The name is: " + polygon.getName())
print("The area is: " + str(polygon.area()))
print("The perimeter is: " + str(polygon.perimeter()))

