from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import User, UserOut, Token
from app.models.user import UserDB
from app.database.connection import get_db
from app.auth.auth_handler import create_access_token, verify_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: User, db: Session = Depends(get_db)):
    if db.query(UserDB).filter(UserDB.username == user.username).first():
        raise HTTPException(status_code=400, detail="User already exists")
    
    db_user = UserDB(username=user.username, password=user.password, is_admin=user.is_admin)
    db.add(db_user)
    db.commit()
    return db_user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == form_data.username, UserDB.password == form_data.password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(user.username, user.is_admin)
    return {"access_token": access_token, "token_type": "bearer"}
