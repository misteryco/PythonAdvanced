def even_numbers(x: str):
    list_of_numbers = [int(y) for y in x.split(", ") if int(y) % 2 == 0]
    return list_of_numbers
# ==========================================
#     below is a solution made only with list comprehension
# matrx_lines = int(input())
# matrx = [[int(y) for y in input().split(", ") if int(y) % 2 == 0] for i in range(matrx_lines)]
# print(matrx)
#
# ===========================================
#
# the solution out of the commented section is made with list comprehension and function
#
#  ==========================================


matrx_lines = int(input())
matrx = [even_numbers(input()) for i in range(matrx_lines)]
print(matrx)
