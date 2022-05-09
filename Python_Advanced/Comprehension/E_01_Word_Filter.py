even_length_list = [print(word) for word in input().split() if not len(word) % 2]

# This is example for a bad practice - it is not a good idea to print in
# the list comprehension. The good i that it is not very often to print on python console.split(", ")

# The preferred printing method is :
#
# for word in even_length_list:
#     print(word)
