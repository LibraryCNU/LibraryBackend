from src.main.data.database.seat_data_source import SeatDataSource
from src.main.domain.repository.seat_repository import SeatRepository


class SeatRepositoryImpl(SeatRepository):
    def __init__(self, data_source: SeatDataSource):
        self.data_source = data_source


