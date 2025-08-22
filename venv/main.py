from fastapi import APIRouter
from fastapi import FastAPI
from app.shema.UsersSchema import usersshema
from app.database.conexion import conn
from app.model.UsersModel import users

app = FastAPI()

@app.get('/')
def root():
    return {'nombre': "desconocido", 'edad': 30}

@app.post('/post')
def createUsers(dataUsers: usersshema):
    newUser = dataUsers.dict()
    with conn.begin():
        conn.execute(users.insert().values(newUser))
    return "registro ingresado"