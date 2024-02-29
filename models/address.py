from sqlalchemy import Column, DateTime, String, Integer, func
from models import Base

class addressModel(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    address = Column(String)
    create_at = Column(DateTime, default=func.now())

    def __repr__(self): 
        return f"id: {self.id}, name: {self.name}"