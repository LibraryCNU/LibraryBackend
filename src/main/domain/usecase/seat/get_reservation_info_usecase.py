from src.main.domain.repository.seat_repository import SeatRepository


class GetReservationInfoUseCase:
    def __init__(self, repository: SeatRepository):
        self.repository = repository

    def execute(self, id: int, place: str = None) -> dict:
        return self.repository.get_reserve_info(id=id, place=place)
