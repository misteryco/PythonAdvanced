rows, columns = [int(x) for x in input().split(", ")]
matrx = []
sub_matrx = []
sub_matrx_sum = 0

for row in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrx.append(row_data)

for r in range((rows-1), 0, -1):
    for c in range(columns-1, 0, -1):
        # print(f"{r},{c}")
        this_sub_matrx = [[matrx[r-1][c-1], matrx[r-1][c]], [matrx[r][c-1], matrx[r][c]]]
        sum_this_sub_matrx = sum([this_sub_matrx[r][c] for r in range(2) for c in range(2)])
        if sum_this_sub_matrx >= sub_matrx_sum:
            sub_matrx = this_sub_matrx
            sub_matrx_sum = sum_this_sub_matrx

print(" ".join([str(sub_matrx[0][c]) for c in range(2)]))
print(" ".join([str(sub_matrx[1][c]) for c in range(2)]))

print(sub_matrx_sum)
