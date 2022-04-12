number_dragons = int(input())
dragons_data = {}
for dragon in range(number_dragons):
    dragon_info = input().split()
    d_type = dragon_info[0]
    d_name = dragon_info[1]
    #STATS :
    d_damage = 45
    if dragon_info[2] != "null":
        d_damage = int(dragon_info[2])

    d_health = 250
    if dragon_info[3] != "null":
        d_health = int(dragon_info[3])

    d_armor = 10
    if dragon_info[4] != "null":
        d_armor= int(dragon_info[4])

    if d_type in dragons_data:
        dragons_data[d_type][d_name] = [d_damage, d_health, d_armor]
    else:
        dragons_data[d_type] = {d_name:[d_damage, d_health, d_armor]}
# print(dragons_data)

type_average = {}

for type_, names in dragons_data.items():
    dict_len = len(dragons_data[type_])
    sum_damage = 0
    sum_health = 0
    sum_armor = 0
    for name, stat in names.items():
        sum_damage += stat[0]
        sum_health += stat[1]
        sum_armor += stat[2]
    type_average[type_] = [sum_damage/dict_len, sum_health/dict_len, sum_armor/dict_len]

for type1, name1 in dragons_data.items():
    print(f"{type1}::({type_average[type1][0]:.2f}/{type_average[type1][1]:.2f}/{type_average[type1][2]:.2f})")
    for name in name1:
        print(f"-{name} -> damage: {dragons_data[type1][name][0]}, health: {dragons_data[type1][name][1]}, armor: {dragons_data[type1][name][2]}")