import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, text

dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
dotenv_path = os.path.abspath(dotenv_path)

load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metaData = MetaData()

