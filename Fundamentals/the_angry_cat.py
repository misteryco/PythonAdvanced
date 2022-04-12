list_of_items = [int(x) for x in input().split(", ")]
cat_index = int(input())
type_of_items = input()

left_list = list_of_items[:cat_index]
right_list = list_of_items[(cat_index+1):]

entry_point_value = list_of_items[cat_index]

left_cheap_list = [x for x in left_list if x < entry_point_value]
left_expensive_list = [x for x in left_list if x >= entry_point_value]

right_cheap_list = [x for x in right_list if x < entry_point_value]
right_expensive_list = [x for x in right_list if x >= entry_point_value]

position = "Right"
sum_of_prices = 0
if type_of_items == "cheap":
    if sum(left_cheap_list) >= sum(right_cheap_list):
        position = "Left"
        sum_of_prices = sum(left_cheap_list)
    else:
        sum_of_prices = sum(right_cheap_list)
if type_of_items == "expensive":
    if sum(left_expensive_list) >= sum(right_expensive_list):
        position = "Left"
        sum_of_prices = sum(left_expensive_list)
    else:
        sum_of_prices = sum(right_expensive_list)

print(f"{position} - {sum_of_prices}")
