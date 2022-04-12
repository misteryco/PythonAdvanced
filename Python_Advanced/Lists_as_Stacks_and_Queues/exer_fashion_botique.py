clothes = input().split()
rack_capacity = int(input())
racks_used = 0
available_space_in_rack = rack_capacity
while clothes:
    this_package = int(clothes[-1])
    if 0 < this_package <= available_space_in_rack:
        if racks_used == 0:
            racks_used += 1
        available_space_in_rack -= this_package
        clothes.pop()
        if available_space_in_rack == 0:
            racks_used += 1
            available_space_in_rack = rack_capacity
    else:
        if this_package != 0:
            racks_used += 1
            available_space_in_rack = rack_capacity - this_package
            clothes.pop()
print(racks_used)