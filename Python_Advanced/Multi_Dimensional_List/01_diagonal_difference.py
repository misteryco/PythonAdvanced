matrix_size = int(input())
matrix = []
for row in range(matrix_size):
    row_d = [int(x) for x in input().split(", ")]
    matrix.append(row_d)

primary_d_sum = 0
secondary_d_sum = 0
counter = 0
for i in range(matrix_size):
    primary_d_sum += matrix[i][i]
for r in range(-1, -1*(matrix_size+1), -1):
    for c in range(matrix_size):
        if c == -(r + 1):                          # (-1*r - 1)
            secondary_d_sum += matrix[r][c]

# print(primary_d_sum)
# print(secondary_d_sum)
print(abs(primary_d_sum - secondary_d_sum))
