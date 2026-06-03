from shape import Shape
from math import sqrt


class Triangle(Shape):
    def __init__(self, shape_id, shape_type, a, b, c):
        super().__init__(shape_id, shape_type)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = self.get_perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c

    def to_dict(self):
        return {
            "ID": self.id,
            "Type": self.type,
            "Side_A": self.a,
            "Side_B": self.b,
            "Side_C": self.c,
            "Area": self.get_area(),
            "Perimeter": self.get_perimeter()
        }