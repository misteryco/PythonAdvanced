from _collections import deque

kids = deque(input().split())
toss = int(input())
counter = 0
while len(kids) > 1:
    counter +=1
    if counter % toss == 0:
        print(f"Removed {kids.popleft()}")
    else:
        kids.append(kids.popleft())
print(f"Last is {kids.popleft()}")