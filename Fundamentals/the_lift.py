capacity = 4
peoples = int(input())
cabins = list(map(lambda x: int(x), input().split()))
for index_cabin in range(len(cabins)):
    current_available_space = capacity - cabins[index_cabin]
    if current_available_space > 0:
        if peoples > current_available_space:
            peoples -= current_available_space
            cabins[index_cabin] += current_available_space
        else:
            cabins[index_cabin] += peoples
            peoples = 0

if peoples == 0 and sum(cabins) == (len(cabins) * capacity):
    print(" ".join([str(x) for x in cabins]))
elif sum(cabins) < (len(cabins) * capacity):
    print(f"The lift has empty spots!")
    print(" ".join([str(x) for x in cabins]))
else:
    print(f"There isn't enough space! {peoples} people in a queue!")
    print(" ".join([str(x) for x in cabins]))