from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from .database.connection import get_db
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from app.shema.users.UsersShema import LoginSchema
from app.controllers.users.UsersControllers import create_user
from app.models.users.UsersModel import users
from sqlalchemy import select

router = APIRouter(prefix='/auth', tags=['auth'])

SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a362006e05a1a23c2fa1270fe3'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class Token(BaseModel):
    access_token: str
    token_type: str 

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/token", response_model=Token)
def  loginAccessToken(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Correo o contraseña incorrectos')
    token_expires = timedelta(minutes=20)
    token = create_access_token(user["email"], user["id"],user["rol"], token_expires)
    return {"access_token": token, "token_type": "bearer"}
 
def authenticate_user(email:str, password:str, db):
    query = select(users).where(users.c.email == email)
    result = db.execute(query).first()
    if not result:
        return False
    user_dict = dict(result._mapping)
    if not bcrypt_context.verify(password, user_dict["contrasenaHash"]):
        return False
    return user_dict

def create_access_token(email:str, userId: int,role:str, expiresDelta: timedelta):
    encode = {'sub':email, 'id':userId, "role": role}
    expires = datetime.utcnow() + expiresDelta
    encode.update({'exp': expires})
    return jwt.encode(encode,SECRET_KEY, algorithm=ALGORITHM)

async def getCurrent(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        userId:int = payload.get('id')
        role: str = payload.get("role")
        if email is None or userId is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='could not validate')
        return {'email':email, 'id':userId, 'role':role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='could not validate user')
    

