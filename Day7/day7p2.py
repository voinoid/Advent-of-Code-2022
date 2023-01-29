f = open("input7.txt", "r")
data = f.readlines()
# print(data)
dir_file_sizes = {"/": [], }
dir_files = {}
current_dir = []
temp_count = 0
# populates the data_dict with all directories and files
for item in data:
    # deals with $ commands
    if item[0:4] == "$ cd":
        if item[5] == "/":
            current_dir = ["/"]
            continue
        if item[5:7] == "..":
            current_dir.pop()
            continue

        dir_name = item[5:-1]
        current_dir.append(dir_name)
        dir_as_string = "".join(current_dir)
        if dir_as_string not in dir_file_sizes:
            dir_file_sizes[dir_as_string] = []
        if temp_count < 20:
            print(dir_file_sizes)
            temp_count += 1
        continue

    # deals with $ ls dir
    if item[0:3] == "dir" or item[0:4] == "$ ls":
        # this is a directory, ignore
        continue

    # print(current_dir)
    # else, if it is not a command or a directory, it must be a file
    if item not in dir_files:
        file = item.split()
        file_size = int(file[0])
        dir_files[item] = ""
        # place file under each directory
        for i in range(len(current_dir)):
            dir_file_sizes["".join(current_dir[0:i+1])] += [file_size]

# print(dir_file_sizes)

# add the sizes of the files in each dir and add them on the end.
big_files = []
for key in dir_file_sizes:
    # overwrites all the file sizes (for now)
    dir_file_sizes[key] = sum(dir_file_sizes[key])
    if dir_file_sizes[key] >= 358913:
        big_files.append(dir_file_sizes[key])
print(30_000_000 - (70_000_000 - dir_file_sizes["/"]))
print(big_files)
print(min(big_files))
