from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_id, shape_type, width, height):
        super().__init__(shape_id, shape_type)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def to_dict(self):
        return {
            "ID": self.id,
            "Type": self.type,
            "Width": self.width,
            "Height": self.height,
            "Area": self.get_area(),
            "Perimeter": self.get_area()
            }