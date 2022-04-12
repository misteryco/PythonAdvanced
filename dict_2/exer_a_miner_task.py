data = input()
data_list = []
while data != "stop":
    data_list.append(data)
    data = input()
# print(data_list)
resources = {}
for idx in range(len(data_list)):
    if idx % 2 == 0:
        if data_list[idx] in resources:
            resources[data_list[idx]] += int(data_list[idx+1])
        else:
            resources[data_list[idx]] = int(data_list[idx + 1])

for nam, amount in resources.items():
    print(f"{nam} -> {amount}")