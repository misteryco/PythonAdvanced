value = input()
total_price = 0

special = False

while True:
    if value == "regular":
        break
    if value == "special":
        special = True
        break
    current_price = float(value)
    if current_price < 0 :
        print("Invalid price!")
        value = input()
        continue
    total_price += current_price
    value = input()

taxes = 0.2 * total_price
total_price_with_taxes = total_price + taxes

if total_price == 0:
    print(f"Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    if not special:
        print(f"Total price: {total_price_with_taxes:.2f}$")
    else:
        special_price = total_price_with_taxes - 0.1 * total_price_with_taxes
        print(f"Total price: {special_price:.2f}$")
