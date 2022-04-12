values = input()
total_sum = 0

special = False

while True:
    if values == "special":
        special = True
        break
    if values == "regular":
        break
    values = float(values)
    if values < 0:
        print(f"Invalid price!" )
        values = 0
    total_sum += values
    values = input()

if total_sum > 0:
    taxes = 0.2 * total_sum
    print(f"Congratulations you've just bought a new computer!")
    total_price_with_taxes = total_sum + taxes
    if special:
        total_price_with_taxes = total_price_with_taxes - 0.1 * total_price_with_taxes
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")
else:
    print(f"Invalid order!")

