
f = open("input2.txt", "r")
data = f.readlines()
scores = {"elf": 0,
          "player": 0}
move_table = {"A": 1,
              "B": 2,
              "C": 3,
              }
elf_win =   {1: 3,
            2: 1,
            3: 2,
            }
elf_lose =   {1: 2,
            2: 3,
            3: 1,
            }
for item in data:
    elf_move = move_table[item[0]]
    result = item[2]

    if result == "Y":
        scores["elf"] += elf_move + 3
        scores["player"] += elf_move + 3
    elif result == "X":
        scores["elf"] += elf_move + 6
        scores["player"] += elf_win[elf_move]
    else:
        scores["elf"] += elf_move
        scores["player"] += elf_lose[elf_move] + 6

    print(scores["elf"])
    print(scores["player"])
