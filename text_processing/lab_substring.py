chars = input()
second_chars = input()
res = ""
while chars in second_chars:
    second_chars = second_chars.replace(chars, "")
print(second_chars)