from sqlalchemy import Column, String, Boolean

from src.main.data.database.database import Base


class BookModel(Base):
    __tablename__ = 'book'
    author = Column(String(255))
    name = Column(String(255), primary_key=True)
    publish = Column(String(255))
    isbn = Column(String(255))
    language = Column(String(255))
    picture = Column(String(1000))
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

    def to_dict(self):
        return {
            "author": self.author,
            "name": self.name,
            "publish": self.publish,
            "isbn": self.isbn,
            "language": self.language,
            "picture": self.picture,
            "is_favorite": self.is_favorite,
        }
