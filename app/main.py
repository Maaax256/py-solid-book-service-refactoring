from app.book import Book
from app.display_service import DisplayService
from app.print_service import PrintService
from app.serialize_service import SerializeService


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book_service = DisplayService(book)
        elif cmd == "print":
            book_service = PrintService(book)
        elif cmd == "serialize":
            book_service = SerializeService(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")
        return book_service.execute(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
