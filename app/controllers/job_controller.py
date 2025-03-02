from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.job import JobDB
from app.schemas.job import Job, JobOut
from app.database import get_db
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import get_current_user
from typing import List

router = APIRouter()

@router.post("/v1/admin/jobs", response_model=JobOut, dependencies=[Depends(JWTBearer())])
def create_job(job: Job, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if not user["is_admin"]:
        raise HTTPException(status_code=403, detail="Only admin can create jobs")
    
    db_job = JobDB(title=job.title, description=job.description, city_id=job.city_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
