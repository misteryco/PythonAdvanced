def matrx_long_string(ro: int, co: int, stringa: str):
    string_ = stringa
    long_string = ""
    for i in range(ro*co):
        if i < len(string_):
            a = i
        else:
            a = i % len(string_)
        long_string += string_[a]
    return long_string


rows, columns = [int(x) for x in input().split()]
snake = input()
matrx = []

for r in range(rows):
    row = []
    for c in range(columns):
        row.append(0)
    matrx.append(row)

replacement_string = matrx_long_string(rows, columns, snake)
counter = 0

for r in range(rows):
    if r % 2 != 0:
        for column in range(-1, -(columns+1), -1):
            matrx[r][column] = replacement_string[counter]
            counter += 1
    else:
        for column in range(columns):
            matrx[r][column] = replacement_string[counter]
            counter += 1

for r_ in range(rows):
    print("".join([str(x) for x in matrx[r_]]))

# Готино решение на инес със зануляване на коунтера след достигане на дължината на индекса на късия стринг
# тогава не е нужен дълъг стринг !
#  Задължително да тествам със deque !!!!


