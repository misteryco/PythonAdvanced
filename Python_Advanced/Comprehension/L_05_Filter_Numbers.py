def divisible_number(num):
    for i in range(2, 11):
        if num % i == 0:
            return True
    else:
        return False


start = int(input())
end = int(input())


f_matrix = [x for x in range(start, (end + 1)) if divisible_number(x)]
print(f_matrix)
