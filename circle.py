from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2
    
    def get_perimeter(self):
        return 2 * pi * self.radius
    
    def to_dict(self):
        return {
            "ID": self.id,
            "Type": self.type,
            "Radius": self.radius,
            "Area": self.get_area(),
            "Perimeter": self.get_area()
            }