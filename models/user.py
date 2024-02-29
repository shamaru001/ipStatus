from sqlalchemy import Column, DateTime, String, Integer, func
from models import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    password = Column(Integer)
    create_at = Column(DateTime, default=func.now())

    def __repr__(self): 
        return f"id: {self.id}, name: {self.name}"