input_data1 = input()
resources_data = {}
while input_data1 != "stop":
    input_data2 = int(input())
    resource, quantity = input_data1, input_data2
    # quantity = input_data2
    if resource not in resources_data:
        resources_data[resource] = 0
    resources_data[resource] += quantity
    input_data1 = input()

for r, q in resources_data.items():
    print(f"{r} -> {q}")