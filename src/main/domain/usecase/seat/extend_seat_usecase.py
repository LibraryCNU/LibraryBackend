from src.main.domain.repository.seat_repository import SeatRepository


class ExtendSeatUseCase:
    def __init__(self, repository: SeatRepository):
        self.repository = repository

    def execute(self, id: int, place: str = None) -> bool:
        return self.repository.extend_seat(id=id, place=place)
