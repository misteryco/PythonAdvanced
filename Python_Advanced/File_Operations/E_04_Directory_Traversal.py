import os

extensions_files = {}
files = os.listdir(".")
# print(files)
for file in files:
    extension = file.split(".")[-1]
    if extension not in extensions_files:
        extensions_files[extension] = [file]
    else:
        extensions_files[extension].append(file)
# print(extensions_files)
path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'out_file.txt')
# path_1 = os.path.join('d:' + os.sep, "_Projects", 'out_file.txt')  # specific way to change disk drive
# print(path_1)
with open(path, "w") as out_file:
    for file_ext in sorted(extensions_files):
        out_file.write(f"++extension - .{file_ext}\n")
        for filename in sorted(extensions_files[file_ext]):
            out_file.write(f"-- {filename}\n")
