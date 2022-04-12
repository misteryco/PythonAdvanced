first = ord(input())
second = ord(input())
string = input()
sum = 0
for char in string:
    this_ord = ord(char)
    if first < this_ord < second:
       sum += this_ord
print(sum)