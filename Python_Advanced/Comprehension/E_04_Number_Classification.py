#  dict solution

def dict_of_value_types(nums):
    type_and_values = {}
    for num in nums:
        if num < 0:
            if "Negative" not in type_and_values:
                type_and_values["Negative"] = [str(num)]
            else:
                type_and_values["Negative"].append(str(num))
        else:
            if "Positive" not in type_and_values:
                type_and_values["Positive"] = [str(num)]
            else:
                type_and_values["Positive"].append(str(num))
        if num % 2 == 0:
            if "Even" not in type_and_values:
                type_and_values["Even"] = [str(num)]
            else:
                type_and_values["Even"].append(str(num))
        else:
            if "Odd" not in type_and_values:
                type_and_values["Odd"] = [str(num)]
            else:
                type_and_values["Odd"].append(str(num))
    return type_and_values


# actual solution:
numbers = [int(x) for x in input().split(", ")]
# dict Solution
types_and_values = dict_of_value_types(numbers)
#  actual solution
negative_numbers = [str(value) for value in numbers if value < 0]
positive_numbers = [str(value) for value in numbers if value >= 0]
even_numbers = [str(value) for value in numbers if value % 2 == 0]
odd_numbers = [str(value) for value in numbers if value % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")

print(f"===========================================================================")
#
#  dict solution prints in random order because the dict is not ordered, so it's not good.
#
[print(f"{typ}: {', '.join(values)}") for typ, values in types_and_values.items()]
