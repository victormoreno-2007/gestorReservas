from pydantic import BaseModel
from enum import Enum
from typing import Optional

class roles(str, Enum):
    user = "user"
    admin = "admin"

class usersshema(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    contrasenaHash: str
    rol: roles = roles.user

