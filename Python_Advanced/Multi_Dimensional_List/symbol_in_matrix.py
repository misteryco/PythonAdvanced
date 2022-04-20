size = int(input())
matrx = []
for r in range(size):
    matrx.append([el for el in input()])
search_symbol = input()
flag = False
for r in range(size):
    for c in range(size):
        if matrx[r][c] == search_symbol:
            flag = True
            print(f"({r}, {c})")
            break
    if flag:
        break
if not flag:
    print(f"{search_symbol} does not occur in the matrix")
