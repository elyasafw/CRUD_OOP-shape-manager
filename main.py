from shape_manager import ShapeManager
from square import Square
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon


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
    choice = input("Select shape: ").strip()
    shape_id = get_next_id(manager)

    if choice == "1":
        side = float(input("Enter side: "))
        shape = Square(shape_id, "square", side)
    elif choice == "2":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        shape = Rectangle(shape_id, "rectangle", width, height)
    elif choice == "3":
        radius = float(input("Enter radius: "))
        shape = Circle(shape_id, "circle", radius)
    elif choice == "4":
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        c = float(input("Enter side C: "))
        shape = Triangle(shape_id, "triangle", a, b, c)
    elif choice == "5":
        side = float(input("Enter side: "))
        shape = Hexagon(shape_id, "hexagon", side)
    else:
        print("Invalid choice")
        return

    manager.create_shape(shape)
    print("Shape added successfully")


def show_all_shapes(manager):
    pass


def update_shape(manager):
    pass


def delete_shape(manager):
    pass


def main():
    manager = ShapeManager()

    while True:
        print("\n1. Add shape")
        print("2. Show all shapes")
        print("3. Update shape")
        print("4. Delete shape")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_shape(manager)
        elif choice == "2":
            show_all_shapes(manager)
        elif choice == "3":
            update_shape(manager)
        elif choice == "4":
            delete_shape(manager)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
