from src.main.domain.entity.seat import Seat
from src.main.domain.repository.seat_repository import SeatRepository


class GetSeatInfoUseCase:
    def __init__(self, repository: SeatRepository):
        self.repository = repository

    def execute(self, id: int) -> Seat:
        return self.repository.get_seat(id=id)
