from collections import deque

name = input()
market_queue = deque()
while name != "End":
    if name == "Paid":
        while market_queue:
            print(market_queue.popleft())
    else:
        market_queue.append(name)
    name = input()
print(f"{len(market_queue)} people remaining.")