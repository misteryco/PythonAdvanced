health = 100
bitcoins = 0

rooms_lst = input().split("|")
room_cnt = 0

for room in rooms_lst:
    room_cnt += 1
    current_room = room.split()
    command = current_room[0]
    value = int(current_room[1])
    if command == "potion":
        curr_health = health + value
        if curr_health >= 100:
            curr_health = 100
        gained_hp = curr_health - health
        health = curr_health
        print(f"You healed for {gained_hp} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health <= 0 :
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_cnt}")
            break
        else:
            print(f"You slayed {command}.")
if room_cnt == len(rooms_lst) and health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")