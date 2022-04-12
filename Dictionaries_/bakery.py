products_list = input().split()
dictionary = {}
for index in range(0, len(products_list), 2):
    product = products_list[index]
    quantity = int(products_list[index + 1])
    dictionary[product] = quantity

print(dictionary)