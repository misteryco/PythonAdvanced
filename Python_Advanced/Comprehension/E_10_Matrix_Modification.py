matrix = [[int(x) for x in input().split()] for row in range(int(input()))]
command = input()
while command != "END":
    this_command, r, c, value = command.split()
    r = int(r)
    c = int(c)
    value = int(value)
    if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]):
        if this_command == "Add":
            matrix[r][c] += value
        else:
            matrix[r][c] -= value
    else:
        print(f"Invalid coordinates")
    command = input()
[print(' '.join([str(x) for x in matrix[row]])) for row in range(len(matrix))]
