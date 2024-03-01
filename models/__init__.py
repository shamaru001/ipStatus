import sys
from sqlalchemy import func
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

    @classmethod
    def count_group_by(self, filter_1, filter_2, groupBy):
        with getDB() as session:
            return session.query(func.count(self.id)).filter(filter_1).filter(filter_2).group_by(groupBy).scalar()