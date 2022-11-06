class Book:
    def __init__(
            self, author: str, name: str, publish: str, isbn: str, language: str, picture: str, is_favorite: bool
    ) -> None:
        self.author = author
        self.name= name
        self.publish = publish
        self.isbn = isbn
        self.language = language
        self.picture = picture
        self.is_favorite = is_favorite
