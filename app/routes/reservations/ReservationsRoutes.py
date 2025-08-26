from fastapi import APIRouter, HTTPException
from ...controllers.reservations.ReservationControllers import createReservations, get_all_Reservations, getReservations, updateReservations, deleteReservations
from app.shema.reservations.ReservationsShema import ReservationCreate,ReservationResponse
from typing import List

router = APIRouter()

# Crear usuario
@router.post("/", response_model=ReservationCreate)
def create(reservationData: ReservationCreate):
    return createReservations(reservationData)

# Ver todos los usuarios
@router.get("/", response_model=List[ReservationResponse])
def list_Reservation():
    return get_all_Reservations()

# Ver un usuario por ID
@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_Reservations(reservationId: int):
    result = getReservations(reservationId)
    if not result:
        raise HTTPException(statusCode=404, detail="Usuario no encontrado")
    return result

# Actualizar usuario
@router.put("/{reservation_id}", response_model=ReservationResponse)
def update(reservationId: int, reservationData: ReservationCreate):
    result = updateReservations(reservationData,reservationId)
    if not result:
        raise HTTPException(statusCode=404, detail="Usuario no encontrado")
    return result

# Eliminar usuario
@router.delete("/{reservaton_id}")
def delete(reservationId: int):
    deleteReservations(reservationId)
    return {"message": "Usuario eliminado correctamente"}