from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Enum
from app.database.conexion import engine, metaData


users = Table("users", metaData,
    Column("id", Integer, primary_key=True),
    Column("nombre", String(100), nullable=False),
    Column("email", String(100), unique=True, nullable=False),
    Column("contrasenaHash", String(255), nullable=False),
    Column("rol", Enum("user", "admin"), default="user"))
 
metaData.create_all(engine)
    