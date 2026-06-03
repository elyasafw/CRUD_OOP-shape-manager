# GitHub link:  https://github.com/elyasafw/CRUD_OOP-shape-manager.git

from shape_manager import ShapeManager
from square import Square
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon


def get_positive_float(prompt):
    valid = False
    while not valid:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("\nValue must be greater than 0.")
            else:
                valid = True
        except ValueError:
            print("\nInvalid input. Please enter a number.")
    return value


def get_positive_int(prompt):
    valid = False
    while not valid:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("\nValue must be greater than 0.")
            else:
                valid = True
        except ValueError:
            print("\nInvalid input. Please enter a whole number.")
    return value


def get_next_id(manager):
    if not manager.shapes:
        return 1
    return max(shape.id for shape in manager.shapes) + 1


def add_shape(manager):
    print("\n1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Hexagon")

    choice = input("\nSelect shape: ").strip()
    shape_id = get_next_id(manager)

    if choice == "1":
        side = get_positive_float("Enter side: ")
        shape = Square(shape_id, "square", side)
    elif choice == "2":
        width = get_positive_float("Enter width: ")
        height = get_positive_float("Enter height: ")
        shape = Rectangle(shape_id, "rectangle", width, height)
    elif choice == "3":
        radius = get_positive_float("Enter radius: ")
        shape = Circle(shape_id, "circle", radius)
    elif choice == "4":
        a = get_positive_float("Enter side A: ")
        b = get_positive_float("Enter side B: ")
        c = get_positive_float("Enter side C: ")
        shape = Triangle(shape_id, "triangle", a, b, c)
    elif choice == "5":
        side = get_positive_float("Enter side: ")
        shape = Hexagon(shape_id, "hexagon", side)
    else:
        print("\nInvalid choice...")
        return

    manager.create_shape(shape)
    print("\nShape added successfully!")


def show_all_shapes(manager):
    shapes = manager.get_all_shapes()
    if not shapes:
        print("\nNo shapes found...")
        return
    print()
    for shape in shapes:
        for key, value in shape.to_dict().items():
            print(f"  {key}: {value}")
        print()


def update_shape(manager):
    shape_id = get_positive_int("\nEnter shape id: ")

    shape = next((s for s in manager.shapes if s.id == shape_id), None)
    if not shape:
        print("\nShape not found...")
        return

    shape_type = shape.type.lower()
    new_data = {}

    print()
    if shape_type == "square":
        new_data["side"] = get_positive_float("Enter new side: ")
    elif shape_type == "rectangle":
        new_data["width"] = get_positive_float("Enter new width: ")
        new_data["height"] = get_positive_float("Enter new height: ")
    elif shape_type == "circle":
        new_data["radius"] = get_positive_float("Enter new radius: ")
    elif shape_type == "triangle":
        new_data["a"] = get_positive_float("Enter new side A: ")
        new_data["b"] = get_positive_float("Enter new side B: ")
        new_data["c"] = get_positive_float("Enter new side C: ")
    elif shape_type == "hexagon":
        new_data["side"] = get_positive_float("Enter new side: ")

    manager.update_shape(shape_id, new_data)
    print("\nShape updated successfully!")


def delete_shape(manager):
    shape_id = get_positive_int("\nEnter shape id: ")

    if manager.delete_shape(shape_id):
        print("\nShape deleted successfully!")
    else:
        print("\nShape not found...")


def print_menu():
    print("\n" + "-" * 30)
    print("  1. Add shape")
    print("  2. Show all shapes")
    print("  3. Update shape")
    print("  4. Delete shape")
    print("  5. Exit")
    print("-" * 30)


def main():
    manager = ShapeManager()

    print("\n" + "=" * 30)
    print("      SHAPE MANAGER")
    print("=" * 30)

    running = True
    while running:
        print_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_shape(manager)
        elif choice == "2":
            show_all_shapes(manager)
        elif choice == "3":
            update_shape(manager)
        elif choice == "4":
            delete_shape(manager)
        elif choice == "5":
            print("\nGoodbye!\n")
            running = False
        else:
            print("\nInvalid choice...")


if __name__ == "__main__":
    main()
