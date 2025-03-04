from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class JobDB(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    city_id = Column(Integer, ForeignKey("cities.id", ondelete="CASCADE")) 
    city = relationship("CityDB") 