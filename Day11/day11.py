from Monkey import Monkey

def main(file: str) -> int:
    # Read file
    with open(file, "r") as f:
        data = f.readlines()
    
    # Clean Data
    clean_data = []
    for item in data:
        item = item.strip()
        clean_data.append(item.split(":"))
    # print(clean_data)   

    # Create Monkeys
    monkeys = {}
    lcm = 1
    count = 0
    for index in range(0, len(clean_data), 7):
        monkeys[count] = Monkey(clean_data[index][0], clean_data[index+1][1], clean_data[index+2][1], clean_data[index+3][1], clean_data[index+4][1], clean_data[index+5][1])
        lcm *= monkeys[count].check
        count += 1
        # print(f"{monkeys[index]}\n")

    print(lcm)
    NUM_ROUNDS = 10_000
    # for NUM_ROUNDS
    for index in range(NUM_ROUNDS):
        # for each Monkey
        for monkey in monkeys.keys():
            # for each item a Monkey has
            for item in monkeys[monkey].items:
                new_monkey, worry_level = monkeys[monkey].inspect(item)
                worry_level %= lcm
                monkeys[new_monkey].items.append(worry_level)

            # Clears all Items from bag once all have been passed.
            monkeys[monkey].items = []    

    # Check to see which Monkey has most inspections after NUM_ROUNDS
    inspections = []
    for monkey in monkeys.keys():
        inspections.append(monkeys[monkey].itemsInspected)

    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

if __name__ == "__main__":
    ans = main("Day11/input.txt")
    print(f"The answer is: {ans}")