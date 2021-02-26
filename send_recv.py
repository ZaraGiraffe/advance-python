'''
Я писав ці функції згідно того, як ви писали на уроці і в мене вийшло дуже схоже, тільки значно протіше,
і тому напевно менш правильно. Я просто не обробляв ніяких складних помилок, тому і не писав нічого такого.
'''


from socket import socket

header_size = 10
pack_size = 1024
encoding = 'utf-8'


def sendMsg(conn: socket, massage: bytes, header_size: int = header_size) -> None:
    massage_size = f'{len(massage):{header_size}}'

    conn.send(massage_size.encode(encoding=encoding))
    conn.send(massage)


def readMsg(conn: socket, header_size: int = header_size, size_pack: int = pack_size):
    data = conn.recv(header_size)

    massage_size = int(data.decode(encoding=encoding))
    massage = b''

    while True:
        if massage_size <= size_pack:
            data = conn.recv(massage_size)
            massage += data
            break

        data = conn.recv(size_pack)
        massage_size -= size_pack
        massage += data

    return massage




