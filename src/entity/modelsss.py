from sqlalchemy import func, Boolean, Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    birthday = Column(Date, index=True)
    additional_data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=True)
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship("User", back_populates="contacts", lazy="joined")

class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    avatar = Column(String(250), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    contacts = relationship("Contact", back_populates="user", lazy="joined")
