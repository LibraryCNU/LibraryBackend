from abc import *

from src.main.domain.entity.seat import Seat


class SeatRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all_seat(self) -> list:
        pass

    @abstractmethod
    def get_seat(self, id: int) -> Seat:
        pass

    @abstractmethod
    def reserve_seat(self, id: int, place: str) -> bool:
        pass

    @abstractmethod
    def cancel_seat(self, id: int, place: str) -> bool:
        pass

    @abstractmethod
    def extend_seat(self, id: int, place: str) -> bool:
        pass

    @abstractmethod
    def get_reserve_info(self, id: int, place: str) -> dict:
        pass
