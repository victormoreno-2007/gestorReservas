from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer,Date, Time, Enum
from ...database.connection import  metaData

reservation = Table("reservation", metaData,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("idUsers", Integer, nullable=False),
    Column("idRooms", Integer, nullable=False),
    Column("fecha", Date, nullable=False),
    Column("horaInicio", Time, nullable=False),
    Column("horaFin", Time, nullable=False),
    Column("estado", Enum("pendiente", "confirmada", "cancelada"), nullable=False)
)