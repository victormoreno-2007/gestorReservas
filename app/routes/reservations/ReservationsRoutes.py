from fastapi import APIRouter, HTTPException,Depends
from ...controllers.reservations.ReservationControllers import createReservations, get_all_Reservations, getReservations, updateReservations, deleteReservations, cancelReservations
from app.shema.reservations.ReservationsShema import ReservationCreate,ReservationResponse
from typing import List,Annotated
from app.auth import getCurrent

router = APIRouter()

dependency = Annotated[dict, Depends(getCurrent)]

# Crear reservacion
@router.post("/", response_model=ReservationCreate)
def create(reservationData: ReservationCreate, user:dependency):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return createReservations(reservationData)

# Ver todos los reservacion
@router.get("/", response_model=List[ReservationResponse])
def list_Reservation(user:dependency):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return get_all_Reservations()

# Ver un reservacion por ID
@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_Reservations(reservationId: int, user:dependency):
    result = getReservations(reservationId)
    if not result:
        raise HTTPException(statusCode=404, detail="Usuario no encontrado")
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return result

# Actualizar reservacion
@router.put("/{reservation_id}", response_model=ReservationResponse)
def update(reservationId: int, reservationData: ReservationCreate, user:dependency):
    result = updateReservations(reservationData,reservationId)
    if not result:
        raise HTTPException(statusCode=404, detail="Usuario no encontrado")
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return result

# Eliminar reservacion
@router.delete("/{reservaton_id}")
def delete(reservationId: int, user:dependency):
    deleteReservations(reservationId)
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return {"message": "Usuario eliminado correctamente"}

@router.put("/{reservation_id}/cancel")
def cancel_reservation(reservation_id: int, user: dependency):
    result = cancelReservations(reservation_id)
    if user.get("role") not in ["admin", "users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para crear usuarios")
    return result