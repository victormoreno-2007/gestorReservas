from pydantic import BaseModel
from typing import Optional

class RoomBase(BaseModel):
    nombre: str
    sede: str
    capacidad: int
    recursos: str

class RoomCreate(RoomBase):
    pass 

class RoomResponse(RoomBase):
    id: int  
    