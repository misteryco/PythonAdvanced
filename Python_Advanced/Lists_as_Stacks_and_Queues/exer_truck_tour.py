from collections import deque

pumps = int(input())
possible = []

fuel_data = deque()
km_data = deque()
for pump in range(pumps):
    input_data = input().split()
    fuel = int(input_data[0])
    km = int(input_data[1])
    fuel_data.append(fuel)
    km_data.append(km)
# print(fuel_data)
# print(km_data)
counter = 0
total_fuel = sum(fuel_data)
total_km = sum(km_data)

for idx in range(pumps):
    counter += 1
    # current_fuel_data = deque(copy.deepcopy(fuel_data))
    current_fuel_data = fuel_data
    # current_km_data = deque(copy.deepcopy(km_data))
    current_km_data = km_data
    available_fuel = 0
    available_km = total_km
    for index in range(pumps):
        current_fuel = current_fuel_data[index]
        current_km = current_km_data[index]
        available_fuel += current_fuel
        if available_fuel >= current_km:
            # available_fuel += current_fuel
            available_km -= current_km
        else:
            break
        available_fuel -= current_km
    if available_fuel >= available_km:
        print(idx)
        break
    fuel_data.rotate(-1)
    km_data.rotate(-1)
