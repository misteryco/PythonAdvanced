import os # omdule that works with operating system
# try / except - error handling
try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print(f'File already deleted!')