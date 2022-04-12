from operator import itemgetter
dwarf_input = input()
all_dwarf_data = {}
while dwarf_input != "Once upon a time":
    dwarf_data = dwarf_input.split(" <:> ")
    name = dwarf_data[0]
    color = dwarf_data[1]
    physics = int(dwarf_data[2])
    if color in all_dwarf_data:
        if name in all_dwarf_data[color]:
            if all_dwarf_data[color][name] < physics:
                all_dwarf_data[color][name] = physics
        else:
            all_dwarf_data[color][name] = physics
    else:
        all_dwarf_data[color] = {name:physics}
    dwarf_input = input()
list_of_dwarfs = []
for color in all_dwarf_data:
    for name in all_dwarf_data[color]:
        list_of_dwarfs.append([color, name, all_dwarf_data[color][name]])

print(list_of_dwarfs)

# sorted_by_physics = sorted(list_of_dwarfs, key=itemgetter(2), reverse=True) # двата реда са равностойни
sorted_by_physics = sorted(list_of_dwarfs, key=lambda x: x[2], reverse=True) # двата реда са равностойни
print(sorted_by_physics)
# sorted_by_color = sorted(sorted_by_physics, key=itemgetter(0), reverse=False)
# print(sorted_by_color)
for element in sorted_by_physics:
    print(f"({element[0]}) {element[1]} <-> {element[2]}")