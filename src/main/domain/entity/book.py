class Book:
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
