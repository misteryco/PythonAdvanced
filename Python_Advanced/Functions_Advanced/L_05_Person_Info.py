def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


# To unpack dictionary to function it is necessary to use **{dict} before the dict. And arguments, need to have same
# names as dictionary's keys.


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

