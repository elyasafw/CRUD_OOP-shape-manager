# Shape Manager

A command-line application for managing geometric shapes using OOP and JSON storage.

## Features

- Add shapes: Square, Rectangle, Circle, Triangle, Hexagon
- View all saved shapes with area and perimeter
- Update an existing shape by ID
- Delete a shape by ID
- Data is saved to `shapes.json` and persists between runs

## How to run

```bash
python main.py
```

## Project structure

| File | Description |
|------|-------------|
| `shape.py` | Base class for all shapes |
| `square.py` | Square class |
| `rectangle.py` | Rectangle class |
| `circle.py` | Circle class |
| `triangle.py` | Triangle class |
| `hexagon.py` | Hexagon class |
| `shape_manager.py` | Handles all CRUD operations and JSON persistence |
| `main.py` | Main menu and user interaction |
| `shapes.json` | Saved shapes data |
