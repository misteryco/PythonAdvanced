countries_list = input().split(", ")
capitals_list = input().split(", ")
zipped_ = list(zip(countries_list, capitals_list))
# connected_data = {countries_list[index]: capitals_list[index] for index in range(len(countries_list))}

connected_data = dict(zipped_)

# connected_data = {}
# for _ in range(len(zipped_)):
#     connected_data[zipped_[_][0]] = zipped_[_][1]

for co, ca in connected_data.items():
    print(f"{co} -> {ca}")