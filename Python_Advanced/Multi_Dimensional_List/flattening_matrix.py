rows = int(input())
flat_matrix = []
for r in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    [flat_matrix.append(el) for el in row_data]
    # for element in row_data:
    #     flat_matrix.append(element)
print(flat_matrix)
