def key_material(item):
    if item in items:
        if items[item] >= 250:
            items[item] = items[item] - 250
            return  True


input_data = input()
input_list = []
items = {}

items["shards"] = 0
items["fragments"] = 0
items["motes"] = 0

flag = False

while True:
    splitted_data = input_data.split()
    input_list = splitted_data
    for idx in range(len(input_list)):
        if idx % 2 == 0:
            this_item = input_list[idx+1].lower()
            if this_item in items:
                items[input_list[idx + 1].lower()] += int(input_list[idx])
            else:
                items[input_list[idx + 1].lower()] = int(input_list[idx])

        if key_material("shards"):
            print(f"Shadowmourne obtained!")
            flag = True
            break
        if key_material("fragments"):
            print(f"Valanyr obtained!")
            flag = True
            break
        if key_material("motes"):
            print(f"Dragonwrath obtained!")
            flag = True
            break
    if flag:
        break
    input_data = input()

print(f"shards: {items['shards']}")
print(f"fragments: {items['fragments']}")
print(f"motes: {items['motes']}")
for k, v in items.items():
    if k != "shards":
        if k != "fragments":
            if k != "motes":
                print(f"{k}: {v}")