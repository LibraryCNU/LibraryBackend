from src.main.data.database.book_data_source import BookDataSource
from src.main.domain.repository.book_repository import BookRepository


class BookRepositoryImpl(BookRepository):
    def __init__(self, data_source: BookDataSource):
        self.data_source = data_source

    def search(self) -> list:
        pass
