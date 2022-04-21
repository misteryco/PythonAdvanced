# подваме редове колони които дават дължина на стринга който ще бъде резултат, след това го запълваме последователно с
# малкия стринг
def matrx_long_string(ro: int, co: int, stringa: str):
    string_ = stringa
    long_string = ""
    for i in range(ro*co):
        if i < len(string_):
            a = i
        else:
            a = i % len(string_)
        long_string += string_[a]
    return long_string
# подваме редове колони които дават дължина на стринга който ще бъде резултат, след това го запълваме последователно с
# малкия стринг


string_ = "abcd"
empty_string = ""
for i in range(12):
    if i < len(string_):
        a = i
    else:
        a = i % len(string_)
    empty_string += string_[a]
    print(empty_string)
