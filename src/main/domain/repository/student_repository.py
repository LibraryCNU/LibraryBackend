from abc import *

from src.main.domain.entity.student import Student


class StudentRepository(metaclass=ABCMeta):
    @abstractmethod
    def login(self, id: str, password: str) -> bool:
        pass

    @abstractmethod
    def logout(self, session: str) -> bool:
        pass

    @abstractmethod
    def get_student_info(self, session: str) -> Student:
        pass
