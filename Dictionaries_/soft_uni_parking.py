number_of_commands = int(input())
parking_users_dict = {}
for _ in range(number_of_commands):
    command = input().split()
    current_command = command[0]
    if current_command == "register":
        current_name, current_plate = command[1], command[2]
        if current_name not in parking_users_dict:
            parking_users_dict[current_name] = current_plate
            print(f"{current_name} registered {current_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {current_plate}")
    else:
        current_name = command[1]
        if current_name not in parking_users_dict:
            print(f"ERROR: user {current_name} not found")
        else:
            print(f"{current_name} unregistered successfully")
            del parking_users_dict[current_name]


for name, plate in parking_users_dict.items():
    print(f"{name} => {plate}")