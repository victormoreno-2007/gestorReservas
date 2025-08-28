from sqlalchemy import insert, select,Enum
from ...models.users.UsersModel import users
from app.database.connection import engine
from ...shema.users.UsersShema import  UserBase,UserCreate
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
#crear usuario
def create_user(userData: UserCreate):
    newUser = userData.dict()
    newUser["contrasenaHash"] = bcrypt_context.hash(newUser.pop("password"))
    with engine.begin() as conn:
        result = conn.execute(users.insert().values(newUser))
        user_id = result.lastrowid   
    return {"id": user_id,**newUser}




#ver usuarios
def get_all_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        return [dict(row._mapping) for row in result]
    
# ver un solo usuario
def getUser(userId: int):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.id == userId)).first()
        if result:
            return dict(result._mapping) 
        return None
    
#Para metodo put
def updateUser(dataUser: UserBase, UserId:int):
    with engine.begin() as conn:
        conn.execute(users.update().values(
            nombre = dataUser.nombre,
            email = dataUser.email,
            rol = dataUser.rol
        ).where(users.c.id == UserId))
        result = conn.execute(users.select().where(users.c.id == UserId)).first()
        return dict(result._mapping)  if result else None
    
# eliminar usuario
def deleteUser(userId: int):
    with engine.begin() as conn:
        conn.execute(users.delete().where(users.c.id == userId))
