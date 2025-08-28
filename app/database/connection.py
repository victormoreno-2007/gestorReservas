import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, declarative_base

dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
dotenv_path = os.path.abspath(dotenv_path)

load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metaData = MetaData()

#SessionLocal: crea sesiones para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base: para definir modelos ORM (tablas en Python)
Base = declarative_base()

#Dependencia que se inyecta en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
