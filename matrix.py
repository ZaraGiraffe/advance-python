from random import randint

'''
У мене колонки у відповіді номеруються з 1
'''


def file_fill(file, rows: int, columns: int) -> None:
    for line in range(rows):
        for integer in range(columns):
            file.write(f"{randint(-20, 20):>4}")
        file.write('\n')


def file_read(file) -> list:
    matrix = []
    for line in file:
        matrix.append(line.split())
    return matrix


def find_rows(n: int, matrix: list) -> list:
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == str(n):
                res.append(i)
                break
    return res


def find_colums(n: int, matrix: list) -> list:
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == str(n):
                res.append(j)
                break
    res = set(res)
    res = list(res)
    return sorted(res)


def matrix_print(matrix: list) -> None:
    for row in matrix:
        for i in row:
            print(f"{i:>4}", end='')
        print()



rows = 10
columns = 10
n = 0

file = open('file.txt', 'w')
file_fill(file, rows, columns)
file.close()

file = open('file.txt', 'r')
matrix = file_read(file)
file.close()

rows = find_rows(n, matrix)
columns = find_colums(n, matrix)

matrix_print(matrix)
print(f'Our number: {n}')
print('Rows (index): ')
for i in rows:
    print(i + 1, end=' ')
print()
print('Columns (index): ')
for i in columns:
    print(i + 1, end=' ')
print()
