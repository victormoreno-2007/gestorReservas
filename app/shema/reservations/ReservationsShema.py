from pydantic import BaseModel
from datetime import date, time
from enum import Enum

class ReservationStatus(str, Enum):
    pendiente = "pendiente"
    confirmada = "confirmada"

class ReservationCreate(BaseModel):
    idUsers: int
    idRooms: int
    fecha: date
    horaInicio: time
    horaFin: time
    estado: ReservationStatus = ReservationStatus.pendiente

class ReservationResponse(BaseModel):
    id: int
    idUsers: int
    idRooms: int
    fecha: date
    horaInicio: time
    horaFin: time
    estado: ReservationStatus