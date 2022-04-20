rows, columns = [int(x) for x in input().split(", ")]
matrix = []
sum_of_values = 0
for r in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)
for idx in range(len(matrix)):
    sum_of_values += sum(matrix[idx])
print(sum_of_values)
print(matrix)
