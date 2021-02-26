'''
Наші бібліотека і книга
'''


class Book:
    def __init__(self, name: str, author: str, year: int, id: int) -> None:
        self.name = name
        self.author = author
        self.year = year
        self.id = id
        self.info = f' - {self.name:<15}{self.author:20}{self.year:<10}{self.id:<10}'

    def __repr__(self) -> str:
        return self.info


class Library:
    def __init__(self):
        '''
        self.books - словник вигляду id:book
        self.info_books_brief - словник вигляду id:book.name
        Останнє я створив чисто для короткого виводу всієї бібліотеки коричстувачем
        '''
        self.books = {}
        self.info_books_brief = {}

    def add_book(self, book: Book) -> None:
        '''
        Додаємо книжку
        '''
        self.books[book.id] = book
        self.info_books_brief[book.id] = book.name

    def del_book(self, id: int) -> bool:
        '''
        Видаляєм книжку по id
        '''
        if id in self.books and id in self.info_books_brief:
            del self.books[id]
            del self.info_books_brief[id]
            return True
        else:
            return False

    def get_book_info(self, id: int) -> str:
        '''
        Видає self.info книги
        '''
        if id in self.books:
            return self.books[id].info

    def get_info(self) -> dict:
        '''
        Видає словник self.info_books_brief
        '''
        return self.info_books_brief

