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
    pass


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
