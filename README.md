# Shape Manager

A system for managing geometric shapes using OOP and JSON storage. Supports two modes: CLI and REST API server.

## Features

- Add shapes: Square, Rectangle, Circle, Triangle, Hexagon
- View all saved shapes with area and perimeter
- Update an existing shape by ID
- Delete a shape by ID
- Get the total count of shapes
- Get the total area of all shapes
- Data is saved to `shapes.json` and persists between runs

## How to run

### CLI mode

```bash
python main.py
```

### Server mode (FastAPI)

```bash
uvicorn server:app --reload
```

#### API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/shapes` | Get all shapes |
| POST | `/shapes` | Add a new shape |
| GET | `/shapes/{id}` | Get a shape by ID |
| PUT | `/shapes/{id}` | Update a shape by ID |
| DELETE | `/shapes/{id}` | Delete a shape by ID |
| GET | `/shapes/count` | Get the total number of shapes |
| GET | `/shapes/total-area` | Get the total area of all shapes |

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
| `main.py` | Main menu and user interaction (CLI) |
| `server.py` | FastAPI server (REST API) |
| `shapes.json` | Saved shapes data |
