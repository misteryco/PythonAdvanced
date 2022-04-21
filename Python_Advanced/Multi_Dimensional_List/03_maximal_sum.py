def micro():
    m = []
    for i in range(3):
        r = []
        for j in range(3):
            r.append(j)
        m.append(r)
    return m, sum(m)


micro_size = 3
micro_matrx = []
micro_sum = 0

rows, columns = [int(x) for x in input().split()]
matrx = []

for r_ in range(rows):
    row_data = [int(x) for x in input().split()]
    matrx.append(row_data)

for r in range(rows-2):
    for c in range(columns-2):
        check_matrx = []
        check_sum = 0
        for i in range(micro_size):
            micro_row = []
            for j in range(micro_size):
                this_value = matrx[r+i][c+j]
                check_sum += this_value
                micro_row.append(matrx[r+i][c+j])
            check_matrx.append(micro_row)
        if check_sum >= micro_sum:
            micro_sum = check_sum
            micro_matrx = check_matrx

print(f"Sum = {micro_sum}")
# print(micro_matrx)
for i in range(micro_size):
    print(" ".join(([str(x) for x in micro_matrx[i]])))
