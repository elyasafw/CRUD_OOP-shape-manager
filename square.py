from shape import Shape


class Square(Shape):
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side= side

    def get_area(self):
        return self.side * self.side
    
    def get_perimeter(self):
        return 4 * self.side
    
    def to_dict(self):
        return {
            "ID": self.id,
            "Type": self.type,
            "Width": self.side,
            "Area": self.get_area(),
            "Perimeter": self.get_area()
            }