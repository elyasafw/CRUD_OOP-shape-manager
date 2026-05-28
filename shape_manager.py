import json
import os
from square import Square
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon


class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        self.shapes.append(shape)
        self.save_to_json()

    def get_all_shapes(self):
        pass

    def update_shape(self, shape_id, new_data):
        pass

    def delete_shape(self, shape_id):
        pass

    def save_to_json(self):
        with open("shapes.json", "w") as f:
            json.dump([shape.to_dict() for shape in self.shapes], f, indent=4)

    def load_from_json(self):
        if not os.path.exists("shapes.json"):
            return
        with open("shapes.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return
        for item in data:
            shape = self._dict_to_shape(item)
            if shape:
                self.shapes.append(shape)

    def _dict_to_shape(self, data):
        shape_type = data.get("Type", "").lower()
        shape_id = data.get("ID")
        if shape_type == "square":
            return Square(shape_id, "square", data["Side"])
        if shape_type == "rectangle":
            return Rectangle(shape_id, "rectangle", data["Width"], data["Height"])
        if shape_type == "circle":
            return Circle(shape_id, "circle", data["Radius"])
        if shape_type == "triangle":
            return Triangle(shape_id, "triangle", data["Side A"], data["Side B"], data["Side C"])
        if shape_type == "hexagon":
            return Hexagon(shape_id, "hexagon", data["Side"])
        return None
