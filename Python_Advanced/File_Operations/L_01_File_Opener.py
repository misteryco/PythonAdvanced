try:
    a = open("tAAAAAext.txt", "r")
    if a:
        print(f"File found")
except FileNotFoundError:
    print(f"File not found")
