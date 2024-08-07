from sqlalchemy.orm import relationship, Mapped, mapped_column

from db.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]

    tasks = relationship("Task", back_populates="owner")
