from shape import Shape
from math import sqrt


class Hexagon(Shape):
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) / 2) * self.side**2

    def get_perimeter(self):
        return 6 * self.side

    def to_dict(self):
        return {
            "ID": self.id,
            "Type": self.type,
            "Side": self.side,
            "Area": self.get_area(),
            "Perimeter": self.get_perimeter()
        }
