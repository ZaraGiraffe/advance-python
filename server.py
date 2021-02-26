'''
Загалом серевер працює так:
1. Заходимо у віний цикл, щоб постійно працювати з користувачами
(Якщо користувач відклюиться сервер не припинить прицювати)
2. Ми підклюаємся до користувача і відсилаємо йому You are connected
3. Користувач виконує певні дії, в залежності від того яку цифру він надіслав (1, 2, 3, 4, 5):
    1 - Додає книгу (Тут важливо правильно ввести дані name,author,year,id іменно в такому порядку і без проміжків)
    2 - Видаляє книгу по id
    3 - Переглядає повні дані книги по її id
    4 - Переглядає короткі дані всіх книг (id: name)
    5 - Користувач завершує працювати
Користувач фактично може вічно працювати (поки не введе 5)
Для зруності роботи користувача, я зробив окремий клас LibraryClient в модулі client
'''


from lib import *
from send_recv import *


encoding = 'utf-8'
library = Library()
library.add_book(Book('example', 'example', 0, 0))


with socket() as server:
    server.bind(('localhost', 12346))
    server.listen(1)

    while True:
        user, _ = server.accept()
        sendMsg(user, 'You are connected\n'.encode(encoding=encoding))
        while True:
            data = int(readMsg(user).decode(encoding=encoding))

            if data == 5:
                sendMsg(user, 'you chose to finish, bye'.encode(encoding=encoding))
                break

            elif data == 1:
                sendMsg(user, 'you chose to add book'.encode(encoding=encoding))
                book_data_bytes = readMsg(user)
                try:
                    book_data = book_data_bytes.decode(encoding=encoding).strip().split(',')
                    library.add_book(Book(book_data[0], book_data[1], int(book_data[2]), int(book_data[3])))
                except:
                    sendMsg(user, 'invalid syntax'.encode(encoding=encoding))
                else:
                    sendMsg(user, 'the book has been added'.encode(encoding=encoding))

            elif data == 2:
                sendMsg(user, 'you chose to delete book'.encode(encoding=encoding))
                id_bytes = readMsg(user)
                id = int(id_bytes.decode(encoding=encoding))
                if library.del_book(id) is True:
                    sendMsg(user, 'the book has been deleted'.encode(encoding=encoding))
                else:
                    sendMsg(user, 'there is no such id'.encode(encoding=encoding))

            elif data == 3:
                sendMsg(user, 'you chose to see books info'.encode(encoding=encoding))
                id_bytes = readMsg(user)
                id = int(id_bytes.decode(encoding=encoding))
                data = library.get_book_info(id)
                if data is None:
                    sendMsg(user, 'there is no such id'.encode(encoding=encoding))
                else:
                    sendMsg(user, data.encode(encoding=encoding))

            elif data == 4:
                sendMsg(user, 'you chose to get books info'.encode(encoding=encoding))
                readMsg(user)
                data = library.get_info()
                data_new = ''
                for k, v in data.items():
                    data_new += ' - ' + str(k) + ' ' + v + '\n'
                sendMsg(user, data_new.encode(encoding=encoding))



