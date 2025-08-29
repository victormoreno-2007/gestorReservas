from fastapi import APIRouter, HTTPException,Depends
from ...controllers.rooms.RoomsControllers import createRooms, get_all_rooms, getRooms, updateRooms, deleteRooms
from app.shema.rooms.RoomsShema import RoomBase, RoomCreate, RoomResponse
from typing import List,Annotated
from app.auth import getCurrent

router = APIRouter()

dependency = Annotated[dict, Depends(getCurrent)]

# Crear habitacion
@router.post("/", response_model=RoomCreate)
def create(roomData: RoomCreate, user:dependency):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return createRooms(roomData)

# Ver todos las habitaciones
@router.get("/", response_model=List[RoomResponse])
def list_Rooms(user:dependency):
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return get_all_rooms()

# Ver una habitación por ID
@router.get("/{room_id}", response_model=RoomResponse)
def get_Rooms(room_id: int, user:dependency):
    result = getRooms(room_id)
    if not result:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return result

# Actualizar habitación
@router.put("/{room_id}", response_model=RoomResponse)
def update(room_id: int, roomData: RoomBase, user:dependency):
    result = updateRooms(roomData, room_id)
    if not result:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return result

# Eliminar usuario
@router.delete("/{room_id}")
def delete(roomId: int, user:dependency):
    deleteRooms(roomId)
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return {"message": "Usuario eliminado correctamente"}