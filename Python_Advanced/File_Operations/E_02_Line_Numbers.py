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


rows_data = []
# clean_test_file()  # Uncomment this line if you have you want standard content in "text.txt"
with open("text.txt", "r") as file:
    for idx, line in enumerate(file):
        all_non_punctuation = len(re.findall('[a-zA-Z]', line))
        all_with_punctuation = sum([len(word) for word in line.split()])
        rows_data.append(f"Line {idx+1}: {line.strip()} ({all_non_punctuation})"
                         f"({all_with_punctuation - all_non_punctuation})\n")

with open("output.txt", "w") as file_out:
    [file_out.write(line) for line in rows_data]
