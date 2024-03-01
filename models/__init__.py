import sys
from sqlalchemy.ext.declarative import declarative_base
from db import getDB


Base = declarative_base()
metadata = Base.metadata

class Model():

    @classmethod
    def findAll(self, consult):
        with getDB() as session:
            return session.scalars(consult).fetchall()
    
    @classmethod
    def findOne(self, column, id):
        with getDB() as session:
            return session.query(self).filter(column == id).first()

    
    def create(self):
        with getDB() as session:
            session.add(self)
            session.commit()