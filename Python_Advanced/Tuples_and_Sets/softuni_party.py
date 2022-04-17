number_of_guests = int(input())
guest_vip_list = set()
guest_not_vip_list = set()
arrived_guests = set()
for r in range(number_of_guests):
    reservation = input()
    if reservation[0].isdigit():
        guest_vip_list.add(reservation)
    else:
        guest_not_vip_list.add(reservation)
arrived = input()
while arrived != "END":
    arrived_guests.add(arrived)
    arrived = input()


guest_vip_list.difference_update(arrived_guests)
guest_not_vip_list.difference_update(arrived_guests)
print(f"{len(guest_vip_list) + len(guest_not_vip_list)}")
for element in sorted(guest_vip_list):
    print(element)

for element in sorted(guest_not_vip_list):
    print(element)