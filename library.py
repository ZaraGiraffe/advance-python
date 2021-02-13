from book_person import *


class Library():
    def __init__(self, people=None, books=None):
        '''
        Створює списки людей та книг
        '''
        if people is None:
            self.people = []
        else:
            self.people = people
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book: Book):
        '''
        Додає книгу в біблтотеку
        '''
        self.books.append(book)

    def del_book(self, book: Book):
        '''
        Видаляє книгу. Якщо книга книги не було в бібліотеці видає відповідну помилку
        Якщо книга була у когось. Вона авдаляється зі списку його книг
        '''
        if book not in self.books:
            print('There is no such book in the library')
        else:
            if book.in_person is not None:
                book.in_person.books.remove(book)
            self.books.remove(book)

    def give_book(self, book: Book, person: Person):
        '''
        Дає книгу людині, але за умови, що книга зареєстрована в бібліотеці, книга - вільна
        та користувач зареєстрований у бібліотеці
        '''
        if person in self.people:
            if book in self.books and book.in_person is None:
                person.books.append(book)
                book.in_person = person
            elif book in self.books and book.in_person is not None:
                print(f'The book is in {book.in_person.name} {book.in_person.surname}')
            else:
                print('The book is not registered in the library')
        else:
            print('Unknown user')

    def take_book(self, book: Book, person: Person):
        '''
        Людина повертає книгу, але за умови, що у неї є ця книга, книга зареєстрована в бібліотеуі
        та користувач зареєстрований у бібліотеці
        '''
        if person in self.people:
            if book in self.books and book in person.books:
                book.in_person = None
                person.books.remove(book)
            elif book in self.books and book not in person.books:
                print(f'There is no such book in {person.name} {person.surname}')
            else:
                print('The book is not registered in the library')
        else:
            print('Unknown user')

    def add_person(self, person: Person):
        '''
        додає користуваа
        '''
        self.people.append(person)

    def del_person(self, person: Person):
        '''
        Видаляє користувача. Якщо у користуваа були книжки, то вони повертаються у бібліотеку
        '''
        if person not in self.people:
            print('There is no such person in the library')
        else:
            for book in person.books:
                self.take_book(book, person)
            self.people.remove(person)

    def print_all_books(self):
        '''
        Виводить усі книги
        '''
        print('All books:')
        for book in self.books:
            print(f' - {book.name:>15}{book.author:>15}{book.id:>8}{book.id:>8}')

    def print_books_available(self):
        '''
        Виводить усі книги, які ще не використовуються кимось
        '''
        print('Available books:')
        for book in self.books:
            if book.in_person is None:
                print(f' - {book.name:>15}{book.author:>15}{book.id:>8}{book.id:>8}')

    def print_books_unavailable(self):
        '''
        Виводить усі книги, які кимось уже використовуються
        '''
        print('Unavailable books:')
        for book in self.books:
            if book.in_person is not None:
                print(f' - {book.name:>15}{book.author:>15}{book.year:>8}{book.id:>8}'
                      f'{" " * 6}is in person: {book.in_person.name}{book.in_person.surname}')

    def sort_books_name(self):
        '''
        Виводить відсортований за іменем список книг
        '''
        dictionary = {}
        for book in self.books:
            dictionary[book.name] = book
        names = sorted(list(dictionary.keys()), key=str)
        for name in names:
            print('Books sorted by name:')
            print(f' - {name:>15}{dictionary[name].author:>15}{dictionary[name].year:>8}{dictionary[name].id:>8}')

    def sort_books_author(self):
        '''
        Виводить відсортований за автором список книг
        '''
        dictionary = {}
        for book in self.books:
            dictionary[book.author] = book
        authors = sorted(list(dictionary.keys()), key=str)
        for author in authors:
            print('Books sorted by name:')
            print(f' - {dictionary[author].name:>15}{dictionary[author].author:>15}{dictionary[author].year:>8}{dictionary[author].id:>8}')

    def sort_books_year(self):
        '''
        Виводить відсортований за роком список книг
        '''
        dictionary = {}
        for book in self.books:
            dictionary[book.year] = book
        years = sorted(list(dictionary.keys()), key=str)
        for year in years:
            print('Books sorted by name:')
            print(f' - {dictionary[year].name:>15}{dictionary[year].author:>15}{dictionary[year].year:>8}{dictionary[year].id:>8}')






