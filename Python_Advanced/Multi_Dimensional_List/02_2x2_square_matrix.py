rows, columns = [int(x) for x in input().split()]
matrx = []
counter = 0
for row_ in range(rows):
    row_data = [x for x in input().split()]
    matrx.append(row_data)
for r in range(rows-1):
    for c in range(columns-1):
        # x1 = matrx[r][c]
        # x2 = matrx[r][c+1]
        # x3 = matrx[r+1][c]
        # x4 = matrx[r+1][c+1]
        if matrx[r][c] == matrx[r][c+1] == matrx[r+1][c] == matrx[r+1][c+1]:
            counter += 1

print(counter)
