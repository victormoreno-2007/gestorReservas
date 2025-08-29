from sqlalchemy import insert, select, update
from ...models.reservations.ReservationsModel import reservation
from app.database.connection import engine
from ...shema.reservations.ReservationsShema import ReservationCreate,ReservationResponse
from fastapi import Depends, ses
from ...database.connection import get_db
from typing import Annotated
from sqlalchemy.orm import Session

db_dependency = Annotated[Session, Depends(get_db)]

#crear reservacion
def createReservations(reservationData: ReservationCreate):
    newreservation = reservationData.dict()
    with engine.begin() as conn:
        conn.execute(reservation.insert().values(newreservation))
    return newreservation

#ver reservacion
def get_all_Reservations():
    with engine.connect() as conn:
        result = conn.execute(reservation.select()).fetchall()
        return [dict(row._mapping) for row in result]
    
# ver una sola sala
def getReservations(reservationId: int):
    with engine.connect() as conn:
        result = conn.execute(reservation.select().where(reservation.c.id == reservationId)).first()
        if result:
            return dict(result._mapping) 
        return None
    
#Para metodo put de reservacion
def updateReservations(reservationData: ReservationCreate, reservationId: int):
    with engine.begin() as conn:
        conn.execute(
            reservation.update().values(
                idUsers = reservationData.idUsers,
                idRooms = reservationData.idRooms,
                fecha = reservationData.fecha,
                horaInicio = reservationData.horaInicio,
                horaFin = reservationData.horaFin,
                estado = reservationData.estado
            ).where(reservation.c.id == reservationId)
        )
        result = conn.execute(reservation.select().where(reservation.c.id == reservationId)).first()
        return dict(result._mapping)  if result else None
    
# eliminar reservacion
def deleteReservations(reservationId: int):
    with engine.begin() as conn:
        conn.execute(reservation.delete().where(reservation.c.id == reservationId))

def cancelReservations(reservationId: int, db:db_dependency):
    query = select(reservation).where(reservation.c.id == reservationId)
    result = db.execute(query).first()
    if not result:
        return None 
    stmt = (update(reservation)
        .where(reservation.c.id == reservationId)
        .values(estado="cancelada")
        .returning(reservation)  
    )
    updated = db.execute(stmt).first()
    db.commit()

    return updated._mapping if updated else None

