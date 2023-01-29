if __name__ == '__main__':
    f = open("Day1/input.txt", "r")
    data = f.readlines()
    total_load = [0]

    for item in data:
        # clean data by removing new lines.
        num = item.rstrip()
        # an empty line indicates a change in Elf and starts with NO load, else add elf's load.
        if num == "":
            total_load.append(0)
        else:
            total_load[-1] += int(num)

    total_load.sort()
    #The Elf carrying the most
    top_load = total_load[-1]
    #The top 3 Elves carrying the most
    top_three_loads = sum(total_load[-3:])

    print(f"Part 1) The heaviest load is: {top_load} caleries.")
    print(f"Part 2) The 3 heaviest loads are: {top_three_loads} caleries.")