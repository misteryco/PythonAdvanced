from collections import deque

pumps_list = deque()
pumps = int(input())
counter = 0
for pump in range(pumps):
    petrol, distance = [int(x) for x in input().split()]
    pumps_list.append((petrol, distance, counter))
    counter += 1

available_fuel = 0
flag = False
for pump_ in range(len(pumps_list)):
    flag = False
    available_fuel = 0
    for idx in range(len(pumps_list)):
        current_pump_fuel = pumps_list[idx][0]
        next_pump_distance = pumps_list[idx][1]
        available_fuel += current_pump_fuel
        if available_fuel >= next_pump_distance:
            available_fuel -= next_pump_distance
        else:
            flag = True
            break
    if flag:
        pumps_list.append(pumps_list.popleft())
    else:
        break
print(pumps_list[0][2])
