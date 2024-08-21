import os

from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
MONGODB_URL = os.environ.get('MONGODB_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

client = MongoClient(MONGODB_URL)
mongodb_db = client['python']
mongodb = mongodb_db['recommend']

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_mongo():
    return mongodb