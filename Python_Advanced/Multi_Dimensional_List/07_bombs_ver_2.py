def logic(ro, co):
    if helper[ro][co] in bombed_list:
        if matrx[ro][co] > 0:
            matrx[ro][co] -= bomb_value
    else:
        matrx[ro][co] -= bomb_value
        bombed_list.append(helper[ro][co])


matrix_size = int(input())
matrx = []
helper = []
bombed_list = []

for row in range(matrix_size):
    matrx.append([int(x) for x in input().split()])
data = input().split()
coordinates = []

count = 0
for i in range(matrix_size):
    ro_w = []
    for j in range(matrix_size):
        count += 1
        ro_w.append(count)
    helper.append(ro_w)

# opredelnqne na koordinati i dobaviane na sila na bombata
for idx in range(len(data)):
    coordinates.append(data[idx].split(","))
    this_r = int(coordinates[idx][0])
    this_c = int(coordinates[idx][1])
    coordinates[idx].append(matrx[this_r][this_c])

for r_c in range(len(coordinates)):
    rc = int(coordinates[r_c][0])
    cc = int(coordinates[r_c][1])
    bomb_value = int(coordinates[r_c][2])
    for mini_row in range(-1, 2, 1):
        for mini_col in range(-1, 2, 1):
            r = rc + mini_row
            c = cc + mini_col
            if 0 <= r < matrix_size:
                if 0 <= c < matrix_size:
                    logic(r, c)

cells_sum = [matrx[i][j] for i in range(matrix_size) for j in range(matrix_size) if matrx[i][j] > 0]
# for i in range(matrix_size):
#     for j in range(matrix_size):
#         if matrx[i][j] > 0:
#             cells_sum.append(matrx[i][j])
print(f"Alive cells: {len(cells_sum)}")
print(f"Sum: {sum(cells_sum)}")
for row in range(matrix_size):
    print(" ".join([str(x) for x in matrx[row]]))
