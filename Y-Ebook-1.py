# https://www.youtube.com/watch?v=1qw5ITr3k9E
class Book:
    def __init__(self, book_id: int, title: str, author: str, content: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.content = content


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name


class UserBookState:
    def __init__(self, user_id: int, book_id: int):
        self.user_id = user_id
        self.book_id = book_id
        self.current_position = 0
        self.font_size = 12
        self.bookmarks = set()


class ReadingService:
    def __init__(self):
        self.books = {}          # book_id -> Book
        self.users = {}          # user_id -> User
        self.states = {}         # (user_id, book_id) -> UserBookState
        self.next_book_id = 1

    def add_book(self, title: str, author: str, content: str) -> int:
        book_id = self.next_book_id
        self.next_book_id += 1

        book = Book(book_id, title, author, content)
        self.books[book_id] = book

        return book_id

    def open_book(self, user_id: int, book_id: int) -> UserBookState:
        key = (user_id, book_id)

        if key not in self.states:
            self.states[key] = UserBookState(user_id, book_id)

        return self.states[key]

    def calculate_chars_per_page(self, font_size: int) -> int:
        # Simplified assumption:
        # larger font size means fewer characters per page.
        base_chars = 1000
        return max(100, base_chars * 12 // font_size)

    def display_page(self, user_id: int, book_id: int) -> str:
        book = self.books[book_id]
        state = self.open_book(user_id, book_id)

        chars_per_page = self.calculate_chars_per_page(state.font_size)

        start = state.current_position
        end = start + chars_per_page

        return book.content[start:end]

    def turn_page(self, user_id: int, book_id: int) -> str:
        book = self.books[book_id]
        state = self.open_book(user_id, book_id)

        chars_per_page = self.calculate_chars_per_page(state.font_size)

        state.current_position = min(
            state.current_position + chars_per_page,
            len(book.content)
        )

        return self.display_page(user_id, book_id)

    def change_font_size(self, user_id: int, book_id: int, font_size: int):
        state = self.open_book(user_id, book_id)
        state.font_size = font_size