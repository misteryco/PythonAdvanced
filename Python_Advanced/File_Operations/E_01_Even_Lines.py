import re


# Function that creates text.txt with few standard content for program test, if you want different input file content,
# don't yse the function below.
def clean_test_file():
    txt_data = ["-I was quick to judge him, but it wasn't his fault.",
                "-Is this some kind of joke?! Is it?",
                "-Quick, hide here. It is safer."]
    start_file = open("text.txt", "w")
    for row in txt_data:
        start_file.write(f"{row} \n")
    start_file.close()


# clean_test_file()  #Uncomment this line if you have you want standard content in "text.txt"
lines = []
try:
    file = open("text.txt", "r")
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            lines.append(list(reversed(list((re.sub(r"[-,.!?]", "@", line).split())))))
    file.close()
except FileNotFoundError:
    print("File not found")
try:
    file = open("text.txt", "w")
    for line_idx in range(len(lines)):
        file.write(f"{' '.join(lines[line_idx])} \n")
except FileNotFoundError:
    print("File not found")
