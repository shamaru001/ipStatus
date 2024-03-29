from sqlalchemy import Column, DateTime, ForeignKey, Integer, func, Boolean
from models import Base, Model
from models.address import addressModel

class statusModel(Base, Model):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True)
    address_id = Column(Integer,  ForeignKey(addressModel.id))
    status = Column(Boolean)
    create_at = Column(DateTime, default=func.now())