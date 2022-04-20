rows, columns = [int(x) for x in input().split(", ")]
matrx = []
for r in range(rows):
    row_data = [int(x) for x in input().split()]
    matrx.append(row_data)
# print(matrx)
for column in range(columns):
    column_sum = 0
    for row in range(rows):
        column_sum += matrx[row][column]
    print(column_sum)
