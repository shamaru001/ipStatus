from sqlalchemy import Column, DateTime, String, Integer, func
from models import Base

class addressModel(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True)
    create_at = Column(DateTime, default=func.now())

