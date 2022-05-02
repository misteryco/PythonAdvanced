def check_even(n):
    if n % 2 == 0:
        return True
    # else:
    #     return False
# It's not necessary to return False !!!


numbers = [int(x) for x in input().split()]

even_numbers = list(filter(check_even, numbers))
print(even_numbers)


# Solution is better with lambda function
even_2 = list(filter(lambda x: x % 2 == 0, numbers))
print(even_2)
