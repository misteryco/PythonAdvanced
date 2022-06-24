# def data_to_matrx(ro):
#     m = []
#     for _ in range(ro):
#         row_data = input().split()
#         m.append(row_data)
#     return m


rows, columns = [int(x) for x in input().split()]

matrx = []
for _ in range(rows):
    row_data = input().split()
    matrx.append(row_data)

command = input().split()

while command[0] != "END":
    flag = False
    if len(command) == 5 and command[0] == "swap":
        r1 = int(command[1])
        c1 = int(command[2])
        r2 = int(command[3])
        c2 = int(command[4])
        if 0 <= r1 < rows and 0 <= r2 < rows:
            if 0 <= c1 < columns and 0 <= c2 < columns:
                val_1 = matrx[r1][c1]
                val_2 = matrx[r2][c2]
                matrx[r1][c1] = val_2
                matrx[r2][c2] = val_1
                for r in range(rows):
                    print(*matrx[r])
            else:
                flag = True
        else:
            flag = True
    else:
        flag = True
    if flag:
        print(f"Invalid input!")
    command = input().split()
