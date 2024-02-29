from sqlalchemy import create_engine
from config import DATABASE_CONNECTION_URI

engine = create_engine(DATABASE_CONNECTION_URI)
def getDB():
    return engine.connect()
        