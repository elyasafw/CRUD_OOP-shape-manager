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


@app.post('/shapes')
def create_shape(new_shape: ShapeModel):
    next_id = len(MANAGER.shapes) + 1
    clean_shape_dict = new_shape.model_dump(exclude_unset=True)
    clean_shape_dict["ID"] = next_id
    for shape in MANAGER.shapes:
        if shape.id == next_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Shape id already in shapes list !"
                )
    new_shape_object = MANAGER._dict_to_shape(clean_shape_dict)
    if not new_shape_object:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid shape type")
    MANAGER.create_shape(new_shape_object)
    return {
        "message": "Shape added successfully",
        "data": new_shape_object.to_dict(),
    }