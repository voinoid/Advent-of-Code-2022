def main() -> None:
    f = open("Day2/input2.txt", "r")
    data = f.readlines()

    scores = {"elf": 0,
              "player": 0}

    move_table = {"A": 1,
                  "B": 2,
                  "C": 3,
                  }

    # Your result table.
    result_table = {"X": "lose",
                    "Y": "draw",
                    "Z": "win",
                    }
    # Gives the points You get if Elf Wins
    elf_win = {1: 3,
               2: 1,
               3: 2,
               }

    # Gives the points You get if Elf loses.
    elf_lose = {1: 2,
                2: 3,
                3: 1,
                }

    # Goes through each move.
    for item in data:
        elf_move = move_table[item[0]]
        result = result_table[item[2]]

        # Assigns the points won in each round.
        if result == "draw":
            scores["elf"] += elf_move + 3
            scores["player"] += elf_move + 3
        elif result == "lose":
            scores["elf"] += elf_move + 6
            scores["player"] += elf_win[elf_move]
        else:
            scores["elf"] += elf_move
            scores["player"] += elf_lose[elf_move] + 6

    print(f"The Elf's final score is: {scores['elf']}")
    print(f'Your final score is: {scores["player"]}')

if __name__ == "__main__":
    main()