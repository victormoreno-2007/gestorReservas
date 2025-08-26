from sqlalchemy import insert, select
from ...models.romms.RoomsModel import rooms
from app.database.connection import engine
from ...shema.rooms.RoomsShema import RoomCreate,RoomBase

#crear sala
def createRooms(roomData: RoomCreate):
    newRoom = roomData.dict()
    with engine.begin() as conn:
        result = conn.execute(rooms.insert().values(newRoom))
        user_id = result.lastrowid
    return {"id": user_id,**newRoom}


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
def updateRooms( roomData: RoomBase, roomId:int ):
    with engine.begin() as conn:
        conn.execute(rooms.update().values(
            nombre = roomData.nombre,
            sede = roomData.sede,
            capacidad = roomData.capacidad,
            recursos = roomData.recursos
        ).where(rooms.c.id == roomId))
        result = conn.execute(rooms.select().where(rooms.c.id == roomId)).first()
        return dict(result._mapping) if result else None
    
# eliminar sala
def deleteRooms(roomId: int):
    with engine.begin() as conn:
        conn.execute(rooms.delete().where(rooms.c.id == roomId))
