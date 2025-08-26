from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    users = "users"
    admin = "admin"

class UserBase(BaseModel):
    nombre: str
    email: str
    rol: RoleEnum = RoleEnum.users

class UserCreate(UserBase):
    contrasenaHash: str 

class UserResponse(UserBase):
    id: int