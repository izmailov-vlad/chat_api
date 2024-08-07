from typing import Optional

from sqlalchemy import ForeignKey, String, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[Optional[str]]
    owner_id = Column(String, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")
