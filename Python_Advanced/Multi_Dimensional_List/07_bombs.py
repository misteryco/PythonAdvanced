matrix_size = int(input())
matrx = []
for row in range(matrix_size):
    matrx.append([int(x) for x in input().split()])
data = input().split()
coordinates = []
for idx in range(len(data)):
    coordinates.append(data[idx].split(","))
    this_r = int(coordinates[idx][0])
    this_c = int(coordinates[idx][1])
    coordinates[idx].append(matrx[this_r][this_c])
# print(coordinates)

for r_c in range(len(coordinates)):
    b_row = int(coordinates[r_c][0])
    b_col = int(coordinates[r_c][1])
    bomb_value = int(coordinates[r_c][2])
    flag = False
    for r in range(matrix_size):
        for c in range(matrix_size):
            if r == b_row and c == b_col:
                # bomb_value = matrx[r][c]
                if bomb_value > 0:
                    if (r - 1) > -1 and (c - 1) > -1:
                        if matrx[r - 1][c - 1] > 0:
                            matrx[r - 1][c - 1] -= bomb_value
                            # print(f"bombed {r-1},{c-1} with value = {bomb_value}")
                    if (r - 1) > -1:
                        if matrx[r - 1][c] > 0:
                            matrx[r - 1][c] -= bomb_value
                            # print(f"bombed {r - 1},{c} with value = {bomb_value}")
                    if (r - 1) > -1 and (c + 1) < matrix_size:
                        if matrx[r - 1][c + 1] > 0:
                            matrx[r - 1][c + 1] -= bomb_value
                        # print(f"bombed {r - 1},{c + 1} with value = {bomb_value}")
                    if (c - 1) > 0:
                        if matrx[r][c - 1] > 0:
                            matrx[r][c - 1] -= bomb_value
                        # print(f"bombed {r},{c - 1} with value = {bomb_value}")
                    if (c + 1) < matrix_size:
                        if matrx[r][c + 1] > 0:
                            matrx[r][c + 1] -= bomb_value
                        # print(f"bombed {r},{c + 1} with value = {bomb_value}")
                    if (r + 1) < matrix_size and (c - 1) > -1:
                        if matrx[r + 1][c - 1] > 0:
                            matrx[r + 1][c - 1] -= bomb_value
                        # print(f"bombed {r + 1},{c - 1} with value = {bomb_value}")
                    if (r + 1) < matrix_size:
                        if matrx[r - 1][c - 1] > 0:
                            matrx[r - 1][c - 1] -= bomb_value
                        # print(f"bombed {r + 1},{c} with value = {bomb_value}")
                    if (r + 1) < matrix_size and (c + 1) < matrix_size:
                        if matrx[r + 1][c + 1] > 0:
                            matrx[r + 1][c + 1] -= bomb_value
                        # print(f"bombed {r + 1},{c + 1} with value = {bomb_value}")
                    matrx[r][c] = 0
                    # print(f"bombed myself {r},{c} with value = {bomb_value}, new value = {matrx[r][c]}")
                    flag = True
                    break
        if flag:
            break

for row in range(matrix_size):
    print(" ".join([str(x) for x in matrx[row]]))
