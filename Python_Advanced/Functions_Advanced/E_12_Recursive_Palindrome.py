def palindrome(string, idx):
    if len(string)-2*idx == 0 or len(string)-2*idx == 1:
        return f"{string} is a palindrome"
    if string[0+idx] == string[len(string)-idx - 1]:
        return palindrome(string, idx + 1)
    else:
        return f"{string} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))