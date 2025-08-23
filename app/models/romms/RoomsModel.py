from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from ...database.connection import  metaData


rooms = Table("rooms", metaData,
    Column("id", Integer, primary_key=True,autoincrement=True),
    Column("nombre", String(100), nullable=False),
    Column("sede", String(50), nullable=False),
    Column("capacidad", Integer, nullable=False),
    Column("recursos", Text, nullable=False))
 
