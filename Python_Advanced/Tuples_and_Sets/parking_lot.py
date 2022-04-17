lines = int(input())
cars = set()
for line in range(lines):
    command, plate = input().split(", ")
    if command == "IN":
        cars.add(plate)
    elif command == "OUT":
        cars.remove(plate)
if len(cars) > 0:
    for plate in cars:
        print(plate)
else:
    print(f"Parking Lot is Empty")
