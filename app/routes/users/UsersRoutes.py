from fastapi import APIRouter, HTTPException
from ...controllers.users.UsersControllers import create_user, get_all_users, getUser, updateUser, deleteUser
from app.shema.users.UsersShema import UserCreate, UserResponse, UserBase
from typing import List

router = APIRouter()

# Crear usuario
@router.post("/", response_model=UserResponse)
def create(userData: UserCreate):
    return create_user(userData)

# Ver todos los usuarios
@router.get("/", response_model=List[UserResponse])
def list_users():
    return get_all_users()

# Ver un usuario por ID
@router.get("/{user_id}", response_model=UserResponse)
def get_User(userId: int):
    result = getUser(userId)
    if not result:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return result

# Actualizar usuario
@router.put("/{user_id}", response_model=UserResponse)
def update(userId: int, user: UserBase):
    result = updateUser(user, userId)
    if not result:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return result

# Eliminar usuario
@router.delete("/{user_id}")
def delete(userId: int):
    deleteUser(userId)
    return {"message": "Usuario eliminado correctamente"}