data = input()
stock_data = {}
total_quantity = 0

while data != "statistics":
    data = data.split(": ")
    product = data[0]
    if product in stock_data:
        stock_data[product] += int(data[1])
    else:
        stock_data[product] = int(data[1])
    data = input()
print(f"Products in stock:")
total_products = 0
for k, v in stock_data.items():
    print(f"- {k}: {v}")
    total_quantity += v
print(f"Total Products: {len(stock_data)}")
print(f"Total Quantity: {total_quantity}")