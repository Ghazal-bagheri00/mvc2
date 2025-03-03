from fastapi import FastAPI
from app.controllers import user_controller, job_controller, city_controller
from app.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_controller.router, prefix="/v1/users", tags=["Users"])
app.include_router(job_controller.router, prefix="/v1/jobs", tags=["Jobs"])
app.include_router(city_controller.router, prefix="/v1/cities", tags=["Cities"])
