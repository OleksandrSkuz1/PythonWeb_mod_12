from datetime import date

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(25), index=True)
    last_name: Mapped[str] = mapped_column(String(25))
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(50), index=True)
    birthday: Mapped[date] = mapped_column(Date(), index=True)
    additional_data: Mapped[str] = mapped_column(String(50), index=True)
    completed: Mapped[bool] = mapped_column(default=False)