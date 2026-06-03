from fastapi import FastAPI, Request, status, HTTPException
from pydantic import BaseModel
import json
import shape_manager as sm



from pydantic import BaseModel


class ShapeModel(BaseModel):
    Type: str
    Area: float
    Perimeter: float

    ID: int | None = None
    Side: float | None = None
    Radius: float | None = None
    Width: float | None = None
    Height: float | None = None
    Side_A: float | None = None
    Side_B: float | None = None
    Side_C: float | None = None


app = FastAPI()

MANAGER = sm.ShapeManager()

 
@app.get('/shapes')
def get_shapes():
    shapes_objects = MANAGER.get_all_shapes()
    shapes_list = [shape.to_dict() for shape in shapes_objects]
    return shapes_list


@app.get('/shapes/{id}')
def get_shape(id: int):
    shapes_objects = MANAGER.get_all_shapes()
    shapes_list = [shape.to_dict() for shape in shapes_objects]
    for shape in shapes_list:
        if shape["ID"] == id:
            return shape
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Shape ID not found in shapes list.."
        )