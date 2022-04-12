pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
maximum_health = int(input())
winner_flag = False
command = input()

while command != "Retire":
    command = command.split()
    current_command = command[0]
    if current_command == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if -1 < index < len(pirate_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                winner_flag = True
                break
    if current_command == "Defend":
        startIndex = int(command[1])
        endIndex = int(command[2])
        damage = int(command[3])
        if (-1 < startIndex < len(pirate_ship)) and (-1 < endIndex < len(pirate_ship)):
            for index in range(len(pirate_ship)):
                if startIndex <= index <= endIndex:
                    pirate_ship[index] -= damage
                    if pirate_ship[index] <= 0:
                        print(f"You lost! The pirate ship has sunken.")
                        winner_flag = True
                        break
    if current_command == "Repair":
        index = int(command[1])
        health = int(command[2])
        if -1 < index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health:
                pirate_ship[index] = maximum_health
    if command[0] == "Status":
        repair_needed = [x for x in pirate_ship if (x / maximum_health) < 0.2]
        count = len(repair_needed)
        print(f"{count} sections need repair.")
    command = input()
if not winner_flag:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")

