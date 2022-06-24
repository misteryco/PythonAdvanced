def valid_coordinates(ro, co):
    if 0 <= ro <= size and 0 <= co <= size:
        return True
    else:
        return False


def next_move(comm, r, c):
    next_r, next_c = None, None
    if comm == "up":
        next_r, next_c = r - 1, c
    elif comm == "down":
        next_r, next_c = r + 1, c
    elif comm == "left":
        next_r, next_c = r, c - 1
    elif comm == "right":
        next_r, next_c = r, c + 1
    return next_r, next_c


size = int(input())
territory = []
alice_row, alice_col = None, None
for row in range(size):
    current_row = input().split()
    for col in range(len(current_row)):
        if current_row[col] == "A":
            alice_row, alice_col = row, col
    territory.append(current_row)

territory[alice_row][alice_col] = "*"
tea_bags = 0
command = input()
while True:
    a_next_r, a_next_c = next_move(command, alice_row, alice_col)
    if valid_coordinates(a_next_r, a_next_c):
        if territory[a_next_r][a_next_c] == ".":
            territory[a_next_r][a_next_c] = "*"
        elif territory[a_next_r][a_next_c].isnumeric():
            tea_bags += int(territory[a_next_r][a_next_c])
            territory[a_next_r][a_next_c] = "*"
            if tea_bags >= 10:
                print(f"She did it! She went to the party.")
                break
        elif territory[a_next_r][a_next_c] == "R":
            territory[a_next_r][a_next_c] = "*"
            print(f"Alice didn't make it to the tea party.")
            break
    else:
        print(f"Alice didn't make it to the tea party.")
        break
    alice_row, alice_col = a_next_r, a_next_c
    command = input()

for row in territory:
    print(" ".join(row))
