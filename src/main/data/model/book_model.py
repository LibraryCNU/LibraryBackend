from sqlalchemy import Column, String, Boolean

from src.main.data.database.database import Base


class BookModel(Base):
    __tablename__ = 'book'
    author = Column(String)
    name = Column(String, primary_key=True)
    publish = Column(String)
    isbn = Column(String)
    language = Column(String)
    picture = Column(String)
    is_favorite = Column(Boolean)

    def __init__(
            self, author: str, name: str, publish: str, isbn: str, language: str, picture: str, is_favorite: bool
    ) -> None:
        self.author = author
        self.name = name
        self.publish = publish
        self.isbn = isbn
        self.language = language
        self.picture = picture
        self.is_favorite = is_favorite
