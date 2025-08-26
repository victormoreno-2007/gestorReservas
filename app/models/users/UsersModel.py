from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Enum
from ...database.connection import metaData


users = Table("users", metaData,
    Column("id", Integer, primary_key=True,autoincrement=True),
    Column("nombre", String(100), nullable=False),
    Column("email", String(100), unique=True, nullable=False),
    Column("contrasenaHash", String(255), nullable=False),
    Column("rol", Enum("users", "admin"), default="users"))
 
