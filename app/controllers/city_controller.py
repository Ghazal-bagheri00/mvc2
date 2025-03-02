from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.city import CityDB
from app.schemas.city import City, CityOut
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/v1/cities", response_model=CityOut)
def create_city(city: City, db: Session = Depends(get_db)):
    db_city = CityDB(name=city.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

@router.get("/v1/cities", response_model=List[CityOut])
def get_cities(db: Session = Depends(get_db)):
    return db.query(CityDB).all()
