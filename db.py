from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_CONNECTION_URI

engine = create_engine(DATABASE_CONNECTION_URI)
Session = sessionmaker(bind=engine)

def getDB():
    return Session()
        