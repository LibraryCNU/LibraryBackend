from abc import *


class BookRepository(metaclass=ABCMeta):
    @abstractmethod
    def search(self) -> list:
        pass
