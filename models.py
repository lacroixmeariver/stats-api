from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from database import Base

class Player(Base):
    __tablename__ = "players"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    position: Mapped[str] = mapped_column(String(20))
    height: Mapped[str] = mapped_column(String(10))
    weight: Mapped[str] = mapped_column(String(10))
    jersey_number: Mapped[str] = mapped_column(String(10))
    college: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(10))
    draft_year: Mapped[int] = mapped_column(Integer)
    draft_round: Mapped[int] = mapped_column(Integer)
    draft_number: Mapped[int] = mapped_column(Integer)

