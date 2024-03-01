import sys
from sqlalchemy.ext.declarative import declarative_base
from db import getDB


Base = declarative_base()
metadata = Base.metadata

class Model():

    @classmethod
    def findAll(self, consult):
        with getDB() as conn:
            return conn.scalars(consult).fetchall()
    
    @classmethod
    def findOne(self, consult):
        with getDB() as conn:
            return conn.scalars(consult).one()

    
    def create(self):
        with getDB() as session:
            session.add(self)
            session.commit()