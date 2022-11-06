from src.main.data.database.database import Database
from src.main.data.model.book_model import BookModel


class BookDataSource:
    def __init__(self, database: Database):
        self.__database = database

    def get_all_book(self) -> list:
        query = self.__database.db.query(BookModel)
        return query

    def get_book(self, name: str) -> BookModel:
        query = self.__database.db.query(BookModel).filter(BookModel.name == name).first()
        return query

    def add_book(
            self, author: str, name: str, publish: str, isbn: str, language: str, picture: str, is_favorite: bool
    ) -> bool:
        book = BookModel(author, name, publish, isbn, language, picture, is_favorite)
        try:
            self.__database.db.add(book)
            self.__database.db.commit()
        except Exception:
            return False
        return True
