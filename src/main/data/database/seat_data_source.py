from datetime import datetime

from src.main.data.database.database import Database
from src.main.data.model.seat_model import SeatModel


class SeatDataSource:
    def __init__(self, database: Database):
        self.__database = database

    def get_all_seat(self) -> list:
        query = self.__database.db.query(SeatModel)
        return query

    def get_seat(self, id: int) -> SeatModel:
        query = self.__database.db.query(SeatModel).filter(SeatModel.id == id)
        return query[0]

    def add_seat(
            self, id: int, place: str, plug_existence: bool, start_time: datetime, end_time: datetime,
            can_reserve: bool, is_favorite: bool
    ) -> bool:
        seat = SeatModel(id, place, plug_existence, start_time, end_time, can_reserve, is_favorite)
        try:
            self.__database.db.add(seat)
            self.__database.db.commit()
        except Exception:
            return False
        return True

    def update_seat(
            self, id: int, place: str = None, plug_existence: bool = None,
            start_time: datetime = None, end_time: datetime = None, can_reserve: bool = None, is_favorite: bool = None
    ) -> bool:
        try:
            updated_data = {}
            if place:
                updated_data[SeatModel.place] = place
            if plug_existence:
                updated_data[SeatModel.plug_existence] = plug_existence
            if start_time:
                updated_data[SeatModel.start_time] = start_time
            if end_time:
                updated_data[SeatModel.end_time] = end_time
            if can_reserve:
                updated_data[SeatModel.can_reserve] = can_reserve
            if is_favorite:
                updated_data[SeatModel.is_favorite] = is_favorite
            self.__database.db.query(SeatModel).filter(SeatModel.id == id).update(updated_data)
            self.__database.db.commit()
        except Exception:
            return False
        return True
