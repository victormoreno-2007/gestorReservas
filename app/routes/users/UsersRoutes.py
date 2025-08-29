from fastapi import APIRouter, HTTPException, Depends
from ...controllers.users.UsersControllers import create_user, get_all_users, getUser, updateUser, deleteUser
from app.shema.users.UsersShema import UserCreate, UserResponse, UserBase
from typing import List, Annotated
from app.auth import getCurrent

router = APIRouter()

dependency = Annotated[dict, Depends(getCurrent)]

# Crear usuario
@router.post("/", response_model=UserResponse)
def create(userData: UserCreate, user:dependency):
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return create_user(userData)


# Ver todos los usuarios
@router.get("/", response_model=List[UserResponse])
def list_users( user:dependency):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return get_all_users()

# Ver un usuario por ID
@router.get("/{user_id}", response_model=UserResponse)
def get_User(userId: int, user:dependency):
    result = getUser(userId)
    if not result:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return result

# Actualizar usuario
@router.put("/{user_id}", response_model=UserResponse)
def update(userId: int, users: UserBase, user:dependency):
    result = updateUser(users, userId)
    if not result:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return result

# Eliminar usuario
@router.delete("/{user_id}")
def delete(userId: int, user:dependency):
    deleteUser(userId)
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return {"message": "Usuario eliminado correctamente"}
