from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    #  notes = relationship("Note", back_populates="user")