def main() -> None:
    f = open("Day2/input2.txt", "r")
    data = f.readlines()

    scores = {"elf": 0,
              "player": 0}

    move_table = {"A": 1,
                  "B": 2,
                  "C": 3,
                  "X": 1,
                  "Y": 2,
                  "Z": 3,
                  }
    # Go through each round
    for item in data:
        elf_move = move_table[item[0]]
        player_move = move_table[item[2]]

        scores["elf"] += elf_move
        scores["player"] += player_move

        move_result = elf_move - player_move

        # Draw
        if elf_move == player_move:
            scores["elf"] += 3
            scores["player"] += 3

        # Elf Wins
        elif move_result == 1 or move_result == -2:
            scores["elf"] += 6

        # You Win
        else:
            scores["player"] += 6

    print(f"The Elf's final score is: {scores['elf']}")
    print(f'Your final score is: {scores["player"]}')

if __name__ == "__main__":
    main()