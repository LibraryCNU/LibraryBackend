from src.main.domain.repository.seat_repository import SeatRepository


class CancelSeatUseCase:
    def __init__(self, repository: SeatRepository):
        self.repository = repository

    def execute(self, id: int, place: str = None) -> bool:
        return self.repository.cancel_seat(id=id, place=place)
