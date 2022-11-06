from src.main.domain.repository.seat_repository import SeatRepository


class GetAllSeatInfoUseCase:
    def __init__(self, repository: SeatRepository):
        self.repository = repository

    def execute(self) -> list:
        return self.repository.get_all_seat()
