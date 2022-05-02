rows, columns = [int(x) for x in input().split()]
# matrix = []
# for r in range(rows):
#     letter_r = chr(r + 97)
#     matrix.append([])
#     for c in range(columns):
#         letter_c = chr(r + c + 97)
#         matrix[r].append(letter_r + letter_c + letter_r)
# print(matrix)
# for r in range(rows):
#     print(" ".join(matrix[r]))
# in this task is visible that comprehension is better solution for some cases


matrix = [[(chr(r + 97) + chr(r + c + 97) + chr(r + 97)) for c in range(columns)] for r in range(rows)]
[print(" ".join(matrix[r])) for r in range(rows)]
