from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("postgresql+psycopg2://myuser:mypassword@127.0.0.1:5432/mydb")


def getDB():
    return engine.connect()
        