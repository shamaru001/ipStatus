from sqlalchemy import Column, DateTime, String, Integer, func
from models import Base, Model

class UserModel(Base, Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    password = Column(String(500))
    create_at = Column(DateTime, default=func.now())
