n = int(input())
matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split()])

print(matrix)
sum_d = 0
for row in range(len(matrix)):
    sum_d += matrix[row][row]
print(sum_d)