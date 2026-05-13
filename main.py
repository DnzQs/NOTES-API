from fastapi import FastAPI

from app.db import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)