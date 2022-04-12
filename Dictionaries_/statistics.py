command = input()
products_table = {}

while command != "statistics":
    command = command.split(": ")
    current_product = command[0]
    current_quantity = int(command[1])
    if current_product not in products_table:
        products_table[current_product] = current_quantity
    else:
        products_table[current_product] += current_quantity
    command = input()

print(f"Products in stock:")

for product in products_table:
    print(f"- {product}: {products_table[product]}")

print(f"Total Products: {len(products_table)}")
print(f"Total Quantity: {sum(products_table.values())}")
# print(f"Total Quantity: {products_table.values()}")
# print(f"Total Quantity: {products_table.keys()}")
