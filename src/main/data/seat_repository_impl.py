from datetime import datetime, timedelta

from src.main.data.database.seat_data_source import SeatDataSource
from src.main.domain.entity.seat import Seat
from src.main.domain.repository.seat_repository import SeatRepository


class SeatRepositoryImpl(SeatRepository):
    def __init__(self, data_source: SeatDataSource):
        self.data_source = data_source

    def get_all_seat(self) -> list:
        seat_models = self.data_source.get_all_seat()
        seats = []
        for i in range(len(list(seat_models))):
            seats.append(Seat(*seat_models[i].to_dict().values()))
        return seats

    def get_seat(self, id: int) -> Seat:
        seat_model = self.data_source.get_seat(id=id)
        if not seat_model:
            return None
        seat = Seat(*seat_model.to_dict().values())
        return seat

    def reserve_seat(self, id: int, place: str) -> bool:
        seat_model = self.data_source.get_seat(id=id)
        if not seat_model:
            return False
        if not seat_model.can_reserve:
            return False
        else:
            self.data_source.update_seat(id=id, can_reserve=False,
                                         start_time=datetime.now(), end_time=datetime.now() + timedelta(hours=4))
            return True

    def cancel_seat(self, id: int, place: str) -> bool:
        seat_model = self.data_source.get_seat(id=id)
        if not seat_model:
            return False
        if seat_model.can_reserve:
            return False
        else:
            self.data_source.update_seat(id=id, can_reserve=True)
            return True

    def extend_seat(self, id: int, place: str) -> bool:
        seat_model = self.data_source.get_seat(id=id)
        if not seat_model:
            return False
        if seat_model.can_reserve:
            return False
        else:
            self.data_source.update_seat(id=id, end_time=seat_model.end_time + timedelta(hours=3))
            return True

    def get_reserve_info(self, id: int, place: str) -> dict:
        seat_model = self.get_seat(id=id)
        if not seat_model:
            return dict()
        reserve_info = {
            'start_time': seat_model.start_time,
            'end_time': seat_model.end_time,
            'can_reserve': seat_model.can_reserve,
        }
        return reserve_info

