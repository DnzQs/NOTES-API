from fastapi import FastAPI

from app.db import Base, engine
from app.routes.auth import router as auth_router
from app.routes.notes import router as notes_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(notes_router)