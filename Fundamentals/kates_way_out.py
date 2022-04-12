count_of_rows = int(input())
maze = []
road_list = []
exit_list = []
for ro in range(count_of_rows):
    r = input()
    r = [x for x in r]
    maze.append(r)
# print(maze)
# print(maze[1][4])
#
k_row_index = 0
k_column_index = 0
max_rows = count_of_rows - 1
max_column = len(maze[0]) -1

for row in range(len(maze)):
    k_row_index = row
    if "k" in maze[row]:
        k_column_index = maze[row].index("k")
        break
# print(k_row_index, k_column_index)
maze[k_row_index][k_column_index] = 1
flag = False
counter = 1
current_point = maze[k_row_index][k_column_index]

current_point = maze[k_row_index][k_column_index]
current_point_row = k_row_index
current_point_col = k_column_index

for i in range(1000):

    if 0 <= (current_point_row -1) <= max_rows and 0 <= (current_point_col - 1) < max_column:
        if maze[current_point_row - 1][current_point_col-1] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row - 1][current_point_col-1] = counter
            current_point_row = current_point_row - 1
            current_point_col = current_point_col-1
            continue

    if 0 <= (current_point_row - 1) <= max_rows and 0 <= (current_point_col - 0) < max_column:
        if maze[current_point_row - 1][current_point_col - 0] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row - 1][current_point_col - 0] = counter
            current_point_row = current_point_row - 1
            current_point_col = current_point_col-0
            continue

    if 0 <= (current_point_row - 1) <= max_rows and 0 <= (current_point_col + 1) < max_column:
        if maze[current_point_row - 1][current_point_col + 1] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row - 1][current_point_col + 1] = counter
            current_point_row = current_point_row - 1
            current_point_col = current_point_col+1
            continue

    if 0 <= (current_point_row - 0) <= max_rows and 0 <= (current_point_col - 1) < max_column:
        if maze[current_point_row - 0][current_point_col - 1] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row - 0][current_point_col - 1] = counter
            current_point_row = current_point_row - 0
            current_point_col = current_point_col-1
            continue

    if 0 <= (current_point_row - 0) <= max_rows and 0 <= (current_point_col + 1) < max_column:
        if maze[current_point_row - 0][current_point_col + 1] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row - 0][current_point_col + 1] = counter
            current_point_row = current_point_row - 0
            current_point_col = current_point_col + 1
            continue

    if 0 <= (current_point_row + 1) <= max_rows and 0 <= (current_point_col - 1) < max_column:
        if maze[current_point_row + 1][current_point_col - 1] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row + 1][current_point_col - 1] = counter
            current_point_row = current_point_row + 1
            current_point_col = current_point_col-1
            continue

    if 0 <= (current_point_row + 1) <= max_rows and 0 <= (current_point_col - 0) < max_column:
        if maze[current_point_row + 1][current_point_col - 0] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row + 1][current_point_col - 0] = counter
            current_point_row = current_point_row + 1
            current_point_col = current_point_col-0
            continue

    if 0 <= (current_point_row + 1) <= max_rows and 0 <= (current_point_col + 1) < max_column:
        if maze[current_point_row + 1][current_point_col + 1] == " ":
            counter += 1
            road_list.append(counter)
            maze[current_point_row + 1][current_point_col + 1] = counter
            current_point_row = current_point_row + 1
            current_point_col = current_point_col+1
            continue


# print(maze)

if current_point_row == 0 or current_point_row == max_rows or current_point_col == 0 or current_point_col == max_column:
    print(f"Kate got out in {(len(road_list) + 1)} moves")
else:
    print(f"Kate cannot get out")

