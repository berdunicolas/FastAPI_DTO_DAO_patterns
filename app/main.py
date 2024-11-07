from fastapi import FastAPI
from .routers.v1 import CoursesRouter
from .db import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(CoursesRouter().router)