from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from src.main.data.database.database import Base


class SeatModel(Base):
    __tablename__ = 'seat'
    id = Column(Integer, primary_key=True)
    place = Column(String(255))
    # TODO make primary key id/place
    plug_existence = Column(Boolean)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    can_reserve = Column(Boolean)
    is_favorite = Column(Boolean)

    def __init__(
            self, id: int, place: str, plug_existence: bool, start_time: datetime, end_time: datetime,
            can_reserve: bool, is_favorite: bool
    ) -> None:
        self.id = id
        self.place = place
        self.plug_existence = plug_existence
        self.start_time = start_time
        self.end_time = end_time
        self.can_reserve = can_reserve
        self.is_favorite = is_favorite
