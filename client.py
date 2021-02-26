'''
Клас для зручної роботи із сервером
Конструктор класу з'єднується з сервером і приймає від нього You are connected
Відповідні цифри (1, 2, 3, 4, 5), які користувач має відсилати на сервер, щоб зробити певні дії
перетворені у відповідні команди:
 1 - add_book
 2 - del_book
 3 - get_book_info
 4 - get_info
 5 - finish
 Також я додав можливість працювати з ним, як із контекстним менеджером (exit викличе finish)

 У мене спочатку часто крашилось, але я ніби все пофіксив.
 Поідеї якщо не робити прям зовсім дурні, сервер не падає
'''


from send_recv import *


class LibraryClient:
    encoding = 'utf-8'

    def __init__(self):
        user = socket()
        user.connect(('localhost', 12346))
        data = readMsg(user)
        print(data.decode(encoding=encoding))
        self.user = user

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish()

    def finish(self):
        sendMsg(self.user, '5'.encode(encoding=encoding))
        data = readMsg(self.user)
        print(data.decode(encoding=encoding))

    def add_book(self, name: str, author: str, year: int, id: int):
        sendMsg(self.user, '1'.encode(encoding=encoding))
        data = readMsg(self.user)
        print(data.decode(encoding=encoding))
        send_data = f'{name},{author},{year},{id}'
        sendMsg(self.user, send_data.encode(encoding=encoding))
        finish = readMsg(self.user)
        print(finish.decode(encoding=encoding), '\n')

    def del_book(self, id: int):
        sendMsg(self.user, '2'.encode(encoding=encoding))
        data = readMsg(self.user)
        print(data.decode(encoding=encoding))
        sendMsg(self.user, str(id).encode(encoding=encoding))
        finish = readMsg(self.user)
        print(finish.decode(encoding=encoding), '\n')

    def get_book_info(self, id: int):
        sendMsg(self.user, '3'.encode(encoding=encoding))
        data = readMsg(self.user)
        print(data.decode(encoding=encoding))
        sendMsg(self.user, str(id).encode(encoding=encoding))
        info = readMsg(self.user)
        print(info.decode(encoding=encoding), '\n')

    def get_info(self):
        sendMsg(self.user, '4'.encode(encoding=encoding))
        data = readMsg(self.user)
        print(data.decode(encoding=encoding))
        sendMsg(self.user, 'give me info'.encode(encoding=encoding))
        info = readMsg(self.user)
        print(info.decode(encoding=encoding), '\n')
