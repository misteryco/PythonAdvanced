houses = [int(x) for x in input().split("@")]
index = 0
max_index = len(houses) - 1
command = input()
while command != "Love!":
    command = command.split()
    current_command = command[0]
    jump = int(command[1])
    index = index + jump
    if index > max_index:
        index = 0
    if houses[index] == 0:
        print(f"Place {houses[index]} already had Valentine's day.")
    elif houses[index] > 0:
        houses[index] -= 2
        if houses[index] == 0:
            print(f"Place {index} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {index}.")
if sum(houses) == 0:
    print(f"Mission was successful.")
else:
    non_zer_houses = [x for x in houses if x > 0]
    print(f"Cupid has failed {len(non_zer_houses)} places.")