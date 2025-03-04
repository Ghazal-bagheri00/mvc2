from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/cities")
def get_cities(db: Session = Depends(get_db)):
    from app.models.city import CityDB  # ⬅️ اینجا واردات را داخل تابع قرار دادم
    return db.query(CityDB).all()

