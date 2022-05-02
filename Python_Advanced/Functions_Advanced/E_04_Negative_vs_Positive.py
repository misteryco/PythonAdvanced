def stronger_value(n1, n2):
    if abs(n1) > abs(n2):
        return f"The negatives are stronger than the positives"
    else:
        return f"The positives are stronger than the negatives"


numbers = [int(x) for x in input().split()]

negative = sum(list(filter(lambda x: x < 0, numbers)))
positive = sum(list(filter(lambda x: x >= 0, numbers)))

print(negative)
print(positive)
print(stronger_value(negative, positive))
