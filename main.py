from fastapi import FastAPI

from app.db import Base, engine
from app.routes import auth
from app.routes import notes


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(notes.router, prefix="/notes", tags=["notes"])