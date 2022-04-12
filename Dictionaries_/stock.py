products_list = input().split()
search_list = input().split()
stock_table = {}

for indx in range(0, len(products_list), 2):
    product = products_list[indx]
    quantity = int(products_list[indx + 1])
    stock_table[product] = quantity

# print(stock_table)

for prodct in search_list:
    if prodct in stock_table:
        print(f"We have {stock_table[prodct]} of {prodct} left")
    else:
        print(f"Sorry, we don't have {prodct}")
