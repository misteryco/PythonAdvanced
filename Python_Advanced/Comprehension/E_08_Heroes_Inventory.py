def summary_of_hero(he):
    items_cost_ = 0
    items_count_ = 0
    for item_, cost_ in heroes_data[he].items():
        items_cost_ += cost_
        items_count_ += 1
    return f"{he} -> Items: {items_count_}, Cost: {items_cost_}"


heroes_data = {hero: {} for hero in input().split(", ")}

command = input()
while command != "End":
    data = command.split("-")
    current_name = data[0]
    current_item = data[1]
    current_cost = int(data[2])
    if current_item not in heroes_data[current_name]:
        heroes_data[current_name][current_item] = current_cost
    command = input()

# for hero in heroes_data:
#     items_cost = 0
#     items_count = 0
#     for item, cost in heroes_data[hero].items():
#         items_cost += cost
#         items_count += 1
#     print(f"{hero} -> Items: {items_count}, Cost: {items_cost}")

[print(summary_of_hero(hero)) for hero in heroes_data]

