
f = open("input2.txt", "r")
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
result_table = {""}
for item in data:
    elf_move = move_table[item[0]]
    player_move = move_table[item[2]]

    scores["elf"] += elf_move
    scores["player"] += player_move

    move_result = elf_move - player_move

    if elf_move == player_move:
        scores["elf"] += 3
        scores["player"] += 3

    elif move_result == 1 or move_result == -2:
        scores["elf"] += 6

    else:
        scores["player"] += 6

    #print(elf_move + '  ' + player_move)
    print(scores["elf"])
    print(scores["player"])
