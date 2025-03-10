from sqlalchemy import Column, Integer, String
from app.database import Base

class CityDB(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

