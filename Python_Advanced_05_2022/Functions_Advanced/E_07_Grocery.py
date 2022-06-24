def grocery_store(**kwargs):
    string = ""
    for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], (-len(x[0]), x[0]))):
        string += f"{k}: {v}\n"
    return string


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))