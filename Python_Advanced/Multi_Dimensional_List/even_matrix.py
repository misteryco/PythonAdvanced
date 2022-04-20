rows = int(input())
matrx = []
for r in range(rows):
    row_data = [int(element) for element in input().split(", ") if int(element) % 2 == 0]
    matrx.append(row_data)
print(matrx)
