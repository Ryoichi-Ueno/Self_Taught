import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

c = Circle(150)
print(c.area())
    
