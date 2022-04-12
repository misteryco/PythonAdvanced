from collections import deque

quantity = int(input())
water_queue = deque()
command = input()
while command != "Start":
    water_queue.append(command)
    command = input()
command = input()
while command != "End":
    split_command = command.split()
    if split_command[0].isdigit():
        liters = int(split_command[0])
        if quantity >= liters:
            quantity -= liters
            print(f"{water_queue.popleft()} got water")
        else:
            print(f"{water_queue.popleft()} must wait")
    elif split_command[0] == "refill":
        refill_litters = int(split_command[1])
        quantity += refill_litters
    command = input()

print(f"{quantity} liters left")