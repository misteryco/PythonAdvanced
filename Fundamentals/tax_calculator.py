cars_list = input().split(">>")

number_of_cars = len(cars_list)
total_taxes = 0

for car in range(number_of_cars):
    current_car = cars_list[car].split()
    type_of_car = current_car[0]
    years_tax = int(current_car[1])
    odometer = int(current_car[2])
    if type_of_car == "family":
        family_tax = (50 - (5 * years_tax)) + (12 * (odometer // 3000))
        total_taxes += family_tax
        print(f"A {type_of_car} car will pay {family_tax:.2f} euros in taxes.")
    elif type_of_car == "heavyDuty":
        heavy_tax = (80 - (8*years_tax)) + (14 * (odometer // 9000))
        total_taxes += heavy_tax
        print(f"A {type_of_car} car will pay {heavy_tax:.2f} euros in taxes.")
    elif type_of_car == "sports":
        sport_tax = 100 - 9 * years_tax + (18 * (odometer // 2000))
        total_taxes += sport_tax
        print(f"A {type_of_car} car will pay {sport_tax:.2f} euros in taxes.")
    else:
        print(f"Invalid car type.")

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")
