def say_smth(n):
    print(f"I'm saying {n}")
    if n == 1:                  # recursion bottom ( base case )
        return
    say_smth(n-1)


say_smth(3)
