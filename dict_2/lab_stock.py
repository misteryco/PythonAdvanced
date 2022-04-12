data = input().split()
product_search = input().split()
stock_data = {}
for idx in range(len(data)):
    if idx % 2 == 0:
        stock_data[data[idx]] = data[idx +1]
for product in product_search:
    if product in stock_data:
        print(f"We have {stock_data[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")