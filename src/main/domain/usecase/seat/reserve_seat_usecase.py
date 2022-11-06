from src.main.domain.repository.seat_repository import SeatRepository


class ReserveSeatUseCase:
    def __init__(self, repository: SeatRepository):
        self.repository = repository

    def execute(self, id: int, place: str = None) -> bool:
        return self.repository.reserve_seat(id=id, place=place)
