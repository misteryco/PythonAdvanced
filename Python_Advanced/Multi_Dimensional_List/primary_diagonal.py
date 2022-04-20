matrix_size = int(input())
matrx = []
diagonal_sum = 0
for r in range(matrix_size):
    row = [int(x) for x in input().split()]
    matrx.append(row)
for d_idx in range(matrix_size):
    diagonal_sum += matrx[d_idx][d_idx]
print(diagonal_sum)
