from abc import ABC, abstractmethod

from app.main import Book


class BookService(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def execute(self, method_type: str) -> None | str:
        pass
