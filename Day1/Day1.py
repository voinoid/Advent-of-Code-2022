if __name__ == '__main__':
    NUM_CARRY = 3
    f = open("input.txt", "r")
    data = f.readlines()
    total_load = [0]
    top_load = 0
    for item in data:
        num = item.rstrip()
        if num == "":
            total_load.append(0)
        else:
            total_load[-1] += int(num)

    total_load.sort()
    top_load = sum(total_load[(-1*NUM_CARRY):])
    #print(total_load)

    print(top_load)