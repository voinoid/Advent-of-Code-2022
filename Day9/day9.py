from operator import add

def move_tail(new_head: list[int], old_tail: list[int]) -> list[int]:
    # Test for NOT moving
    if (abs(new_head[0] - old_tail[0]) <= 1 and abs(new_head[1] - old_tail[1]) <= 1): return old_tail

    # Else tail must move
    new_tail = old_tail
    # For moving Left or right
    horizontal = make_move(new_head[0], old_tail[0])
    new_tail = list( map(add, new_tail, [horizontal, 0]))

    vertical = make_move(new_head[1], old_tail[1])
    new_tail = list( map(add, new_tail, [0, vertical]))

    return new_tail

def move_head(dir: str, old_head: list[int]) -> list[int]:
    new_head = old_head
    if dir == "U":
        new_head[1] = new_head[1] + 1
        return new_head

    if dir == "D":
        new_head[1] = new_head[1] - 1
        return new_head

    if dir == "L":
        new_head[0] = new_head[0] - 1
        return new_head

    if dir == "R":
        new_head[0] = new_head[0] + 1
        return new_head

    return new_head


def make_move(head_pos: int, tail_pos: int) -> int:
    if head_pos > tail_pos: return 1
    if head_pos < tail_pos: return -1
    return 0

def main(file: str, rope: int) -> int:
    with open(file, "r") as f:
        data = f.readlines()

    clean_data = []
    # Starting position is (0,0) and it has definitely been here once.
    places_visited = {"0,0": 1}
    # Starting positions 0 - H, 1 - T
    pos = {"H": [0, 0],
           "T": [0, 0], }

    # For a rope length greater than 2
    for i in range(1, rope-1):
        pos[str(i)] = [0, 0]

    # Clean data
    for item in data:
        item = item.rstrip()
        clean_data.append(item.split(" "))

    for item in clean_data:
        for _ in range(int(item[1])):
            # Move Head
            pos["H"] = move_head(dir=item[0], old_head=pos["H"])

            # Move all the bits between the head and tail.
            for i in range(1, rope-1):
                if i > 1:
                    pos[str(i)] = move_tail(new_head=pos[str(i-1)], old_tail=pos[str(i)])
                else:
                    pos[str(i)] = move_tail(new_head=pos["H"], old_tail=pos[str(i)])

            # Move Tail
            pos["T"] = move_tail(new_head=pos[str(rope -2)], old_tail=pos["T"])

            # Add the tails position to the dictionary/Hashtable
            temp_dic = f'{pos["T"][0]},{pos["T"][1]}'
            if temp_dic in places_visited.keys():
                places_visited[temp_dic] += 1
            else:
                places_visited[temp_dic] = 1
        #print(f"Heads pos: {pos['H']}")
        #print(f"Tails pos: {pos['T']}")
    
    return len(places_visited)

if __name__ == '__main__':
    ans = main("Day9/input.txt", 10)
    print(f"Number of places visited: {ans}")
