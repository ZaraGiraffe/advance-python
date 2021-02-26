'''
with LibraryClient() as user:
    user.get_info()
    user.add_book('asasa', 'asasasas', 2323, 1)
    user.add_book('jkhkhbj', 'dfsngvnd', 3434, 2)
    user.get_info()
    user.get_book_info(1)
    user.del_book(2)
    user.get_book_info(2)
    user.get_info()
'''


from client import LibraryClient

with LibraryClient() as user:
    pass