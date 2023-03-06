def main(file: str) -> list:
    # Read file
    with open(file, "r") as f:
        data = f.readlines()
    
    # Clean Data
    clean_data = []
    for item in data:
        item = item.rstrip()
        clean_data.append(item.split(" "))
    #print(clean_data)   

    # Declare variables
    sum_signals = 0
    register_X = 1
    clock_count = 0
    crt = ""
    
    for item in clean_data:
        # Noop adds a clock cycle only
        if item[0] == "noop":
            # Code to write to crt
            crt += add_crt(register_X=register_X, clock_cycle=clock_count)
            clock_count += 1
            if (clock_count + 20) % 40 == 0: 
                sum_signals += clock_count * register_X
                #print(f"Clock: {clock_count}, {register_X}, 1")
            continue

        # If NOT Noop then must be addx
        for _ in range(2):
            # Code to write to crt
            crt += add_crt(register_X=register_X, clock_cycle=clock_count)
            clock_count += 1
            if (clock_count + 20) % 40 == 0: 
                sum_signals += clock_count * register_X
                #print(f"Clock: {clock_count}, {register_X}, 2")

        register_X += int(item[1])

    return [sum_signals, crt]


def add_crt(register_X: int, clock_cycle: int) -> str:
    crt = ""
    if abs(register_X - (clock_cycle % 40)) <=1:
        crt += "#"
    else:
        crt += "."

    if clock_cycle % 40 == 39:
        crt += "\n"
    
    return crt

if __name__ == "__main__":
    ans = main("Day10/input.txt")
    print(f"The answer is: {ans[0]} and the CRT is:\n\n{ans[1]}")