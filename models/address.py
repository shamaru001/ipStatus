from sqlalchemy import Column, DateTime, String, Integer, func
from models import Base, Model
from sqlalchemy.orm import relationship

class addressModel(Base, Model):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True)
    create_at = Column(DateTime, default=func.now())

