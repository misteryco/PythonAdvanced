matrix = [[int(x) for x in input().split(", ")] for x in range(int(input()))]
# d1 = []
# d2 = []
# # for r in range(len(matrix)):
# #     d1.append(matrix[r][r])
# #     d2.append(matrix[r][(len(matrix) - 1) - r])
#
# It's clear that the solution without comprehension is much more readable and maybe faster.
#
#
print(f"First diagonal: {', '.join([str(matrix[x][x]) for x in range(len(matrix))])}. "
      f"Sum: {sum([matrix[x][x] for x in range(len(matrix))])}")
print(f"Second diagonal: {', '.join([str(matrix[r][(len(matrix) - 1) - r]) for r in range(len(matrix))])}. "
      f"Sum: {sum([matrix[r][(len(matrix) - 1) - r] for r in range(len(matrix))])}")
