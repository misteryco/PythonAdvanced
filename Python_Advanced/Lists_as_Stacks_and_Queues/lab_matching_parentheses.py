a_expression = input()
parentheses_idx = []
for idx in range(len(a_expression)):
    this_symbol = a_expression[idx]
    if a_expression[idx] == "(":
        parentheses_idx.append(idx)
    elif a_expression[idx] == ")":
        print(f"{a_expression[parentheses_idx.pop():(idx+1)]}")
