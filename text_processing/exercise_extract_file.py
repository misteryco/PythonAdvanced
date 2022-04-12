file_path = input().split(chr(92))
file_with_extension = file_path[-1].split(".")
print(f"File name: {file_with_extension[0]}")
print(f"File extension: {file_with_extension[1]}")
