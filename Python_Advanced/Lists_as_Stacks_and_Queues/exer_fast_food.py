from collections import deque

total_available_food = int(input())
orders_string = deque(input().split())
orders = deque()

while orders_string:
    orders.append(int(orders_string.popleft()))
print(max(orders))

while orders:
    this_order = orders[0]
    if this_order <= total_available_food:
        total_available_food -= this_order
        orders.popleft()
    else:
        break

if len(orders) == 0:
    print(f"Orders complete")

else:
    print("Orders left: ", end="")
    print(*orders, end=' ')
