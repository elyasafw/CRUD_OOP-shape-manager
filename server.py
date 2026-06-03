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