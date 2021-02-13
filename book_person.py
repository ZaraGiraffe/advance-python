class Book():
    def __init__(self, id: int, name: str, author: str, year: int):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.in_person = None


class Person():
    def __init__(self, id: int, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.books = []
