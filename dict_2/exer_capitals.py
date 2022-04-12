countries = input().split(", ")
cities = input().split(", ")
# connected_data = {countries[idx]: cities[idx] for idx in range(len(countries))}
connected_data = dict(zip(countries, cities))
for count, city in connected_data.items():
    print(f"{count} -> {city}")
