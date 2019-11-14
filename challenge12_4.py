class Hexisgon:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return self.radius * 6

hx = Hexisgon(50)
print(hx.calculate_perimeter())

        
    
