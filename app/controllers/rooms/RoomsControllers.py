from sqlalchemy import insert, select
from ...models.romms.RoomsModel import rooms
from app.database.connection import engine
from ...shema.rooms.RoomsShema import RoomCreate

#crear sala
def create_room(roomData: RoomCreate):
    newRoom = roomData.dict()
    with engine.begin() as conn:
        conn.execute(rooms.insert().values(newRoom))
    return newRoom

#ver salas
def get_all_rooms():
    with engine.connect() as conn:
        result = conn.execute(rooms.select()).fetchall()
        return [dict(row._mapping) for row in result]
    
# ver una sola sala
def getRooms(roomsId: int):
    with engine.connect() as conn:
        result = conn.execute(rooms.select().where(rooms.c.id == roomsId)).first()
        if result:
            return dict(result._mapping) 
        return None
    
#Para metodo put de sala
def updateRooms(roomData: RoomCreate, roomId:int):
    with engine.connect() as conn:
        conn.execute(rooms.update().values(
            nombre = roomData.nombre,
            sede = roomData.sede,
            capacidad = roomData.capacidad,
            recursos = roomData.recursos
        ).where(rooms.c.id == roomId))
        result = conn.execute(rooms.select().where(rooms.c.id == roomId)).first()
        return dict(result._mapping)
    
# eliminar sala
def deleteRooms(userId: int):
    with engine.connect() as conn:
        conn.execute(rooms.delete().where(rooms.c.id == userId))
