from venv import logger


def get_priority_number(char) -> int:
    # ord(char) a-z is 97-122; A-Z is 65-90
    # It is required that a-z is 1-26 and A-Z is 27-52
    num = ord(char) - 96
    if num < 0:
        num += 58
    return num


def find_duplicates(data: list[str]) -> int:
    priority_count = 0

    for item in data:
        item = item.rstrip()
        n = len(item)//2
        half1 = item[0:n]
        half2 = item[n:]
        char = "".join(set(half1).intersection(half2))
        priority_count += get_priority_number(char)

    return priority_count


def find_badge(data: list[str]) -> int:
    priority_count = 0

    if len(data) % 3 != 0:
        raise Exception("Not all people can be put in a group of 3.")
        
    num_groups = len(data)//3
    
    for group in range(num_groups):
        pack1 = set(data[group*3].rstrip())
        pack2 = set(data[group*3+1].rstrip())
        pack3 = set(data[group*3+2].rstrip())
        char = "".join(set.intersection(pack1, pack2, pack3))
        priority_count += get_priority_number(char)

    return priority_count


def main() -> None:
    try:
        with open("Day3/input3.txt", "r") as f:
            data = f.readlines()
            result1 = find_duplicates(data)
            print(f"The 1st result is: {result1}")
            result2 = find_badge(data)
            print(f"The 2nd result is: {result2}")
    except FileNotFoundError as e:
        logger.error('Failed to find file: ' + str(e))
    except Exception as e:
        logger.error('Unhandled error: ' + str(e))


if __name__ == "__main__":
    main()
