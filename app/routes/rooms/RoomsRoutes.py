from fastapi import APIRouter, HTTPException
from ...controllers.rooms.RoomsControllers import createRooms, get_all_rooms, getRooms, updateRooms, deleteRooms
from app.shema.rooms.RoomsShema import RoomBase, RoomCreate, RoomResponse
from typing import List

router = APIRouter()

# Crear usuario
@router.post("/", response_model=RoomCreate)
def create(roomData: RoomCreate):
    return createRooms(roomData)

# Ver todos los usuarios
@router.get("/", response_model=List[RoomResponse])
def list_Rooms():
    return get_all_rooms()

# Ver una habitación por ID
@router.get("/{room_id}", response_model=RoomResponse)
def get_Rooms(room_id: int):
    result = getRooms(room_id)
    if not result:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return result

# Actualizar habitación
@router.put("/{room_id}", response_model=RoomResponse)
def update(room_id: int, roomData: RoomBase):
    result = updateRooms(roomData, room_id)
    if not result:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return result

# Eliminar usuario
@router.delete("/{room_id}")
def delete(roomId: int):
    deleteRooms(roomId)
    return {"message": "Usuario eliminado correctamente"}