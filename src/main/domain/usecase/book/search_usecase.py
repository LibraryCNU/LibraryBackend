from src.main.domain.repository.book_repository import BookRepository


class SearchUseCase:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> list:
        return self.repository.search()
