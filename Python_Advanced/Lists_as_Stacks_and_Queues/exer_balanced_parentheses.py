from collections import deque

list_of_parentheses = deque(list(input()))

while list_of_parentheses:
    left_value = ord(list_of_parentheses[0])
    right_value_1 = ord(list_of_parentheses[1]) - 2
    right_value_2 = ord(list_of_parentheses[-1]) - 2
    if left_value == 40:
        right_value_1 = right_value_1 + 1
        right_value_2 = right_value_2 + 1
    if len(list_of_parentheses) > 0:
        if left_value == right_value_1:
            list_of_parentheses.popleft()
            list_of_parentheses.popleft()
        elif left_value == right_value_2:
            list_of_parentheses.popleft()
            list_of_parentheses.pop()
        else:
            break
    else:
        break
if len(list_of_parentheses) > 0:
    print("NO")
else:
    print("YES")
