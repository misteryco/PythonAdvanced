def legendary_farming():
    input_list = input().lower()
    input_list = input_list.split()
    win = False
    materials_dict = {"shards": 0, "fragments": 0, "motes": 0}
    junk_dict = {}
    while True:
        for material, quantity in zip(input_list[1::2], input_list[0::2]):
            if material in materials_dict:
                materials_dict[material] += int(quantity)
                if materials_dict[material] >= 250:
                    materials_dict[material] -= 250
                    win = True
                    if material == "shards":
                        legendary_item = "Shadowmourne"
                    elif material == "fragments":
                        legendary_item = "Valanyr"
                    elif material == "motes":
                        legendary_item = "Dragonwrath"
                    print(f"{legendary_item} obtained!")
                    break
            else:
                if material not in junk_dict:
                    junk_dict[material] = 0
                junk_dict[material] += int(quantity)
        if win:
            break
        input_list = input().lower()
        input_list = input_list.split()

    print(f"shards: {materials_dict['shards']}")
    print(f"fragments: {materials_dict['fragments']}")
    print(f"motes: {materials_dict['motes']}")
    for mat, qua in junk_dict.items():
        print(f"{mat}: {qua}")


legendary_farming()