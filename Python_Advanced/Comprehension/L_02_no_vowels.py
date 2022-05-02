def this_is_not_vowel(char):
    if char.lower() in "aouei":
        return False
    else:
        return True


a = [x for x in list(input()) if this_is_not_vowel(x)]
print(a)
