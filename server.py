from fastapi import FastAPI, Request, status, HTTPException
from pydantic import BaseModel
import json
import shape_manager as sm


class CreateShapeModel(BaseModel):
    Type: str
    Area: float
    Perimeter: float

    Side: float | None = None
    Radius: float | None = None
    Width: float | None = None
    Height: float | None = None
    Side_A: float | None = None
    Side_B: float | None = None
    Side_C: float | None = None

class UpdateShapeModel(BaseModel):
    Side: float | None = None
    Radius: float | None = None
    Width: float | None = None
    Height: float | None = None
    Side_A: float | None = None
    Side_B: float | None = None
    Side_C: float | None = None


app = FastAPI()

MANAGER = sm.ShapeManager()

 
@app.get('/shapes', status_code=status.HTTP_200_OK)
def get_shapes():
    shapes_list = [shape.to_dict() for shape in MANAGER.shapes]
    return shapes_list


@app.post('/shapes', status_code=status.HTTP_201_CREATED)
def create_shape(new_shape: CreateShapeModel):
    next_id = len(MANAGER.shapes) + 1
    clean_shape_dict = new_shape.model_dump(exclude_unset=True)
    clean_shape_dict["ID"] = next_id
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


@app.get('/shapes/total-area', status_code=status.HTTP_200_OK)
def calculate_total_shapes():
    shapes_list = [shape.to_dict() for shape in MANAGER.shapes]
    if not shapes_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The shape list is empty..."
            )    
    areas_list = [shape["Area"] for shape in shapes_list]
    return {"message": f"Total area of ​​all shapes: {round(sum(areas_list), 3)}"}


@app.get('/shapes/{id}', status_code=status.HTTP_200_OK)
def get_shape(id: int):
    shapes_list = [shape.to_dict() for shape in MANAGER.shapes]
    for shape in shapes_list:
        if shape["ID"] == id:
            return shape
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Shape ID not found in shapes list.."
        )


@app.put('/shapes/{id}', status_code=status.HTTP_200_OK)
def update_shape(id: int, update_data: UpdateShapeModel):
    clean_updates = update_data.model_dump(exclude_unset=True)
    clean_updates_lower = {k.lower(): v for k, v in clean_updates.items()}
    up_success = MANAGER.update_shape(id, clean_updates_lower)
    if not up_success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shape ID not found in shapes list..."
        )
    return {"message": "Shape updated successfully"}


@app.delete('/shapes/{id}', status_code=status.HTTP_200_OK)
def delete_shape(id: int):
    del_success = MANAGER.delete_shape(id)
    if not del_success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shape ID not found in shapes list...",
        )
    return {"message": f"Shape ID {id} was deleted successfully"}