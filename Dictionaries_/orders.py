def orders():
    command_line = input().split()
    products_dict_list = {}
    while command_line[0] != "buy":
        name_product = command_line[0]
        price = float(command_line[1])
        quantity = int(command_line[2])
        if name_product not in products_dict_list:
            products_dict_list[name_product] = [0.0, 0]
        products_dict_list[name_product][0] = price
        products_dict_list[name_product][1] += quantity
        command_line = input().split()

    # print(products_dict_list)

    for product, info in products_dict_list.items():
        print(f"{product} -> {(info[0] * info[1]):.2f}")


orders()