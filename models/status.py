from sqlalchemy import Column, DateTime, ForeignKey, String, Integer, func, Boolean
from models import Base
from models.address import addressModel

class statusModel(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True)
    ip = Column(String,  ForeignKey(addressModel.id))
    status = Column(Boolean)
    create_at = Column(DateTime, default=func.now())

    def __repr__(self): 
        return f"id: {self.id}, name: {self.name}"