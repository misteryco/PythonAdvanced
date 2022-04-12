loot = input().split("|")
# print(loot)
command = input()
sum_of_string_len = 0
while command != "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        for loot_index in range(1, len(command)):
            if command[loot_index] not in loot:
                loot.insert(0, command[loot_index])
    if command[0] == "Drop":
        drop_index = int(command[1])
        if -1 < drop_index < (len(loot) - 1):
            loot.append(loot.pop(drop_index))
    if command[0] == "Steal":
        stolen_items = []
        count = int(command[1])
        if count > len(loot):
            count = len(loot)
        for item in range(count):
            stolen_items.append(loot.pop(-1))
        stolen_items.reverse()
        print(", ".join(stolen_items))
    command = input()
if len(loot) > 0:
    for element in loot:
        sum_of_string_len += len(element)
    average_treasure_gain = sum_of_string_len / len(loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")
