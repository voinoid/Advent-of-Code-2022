
f = open("input5.txt", "r")
data = f.readlines()
#print(data)
stacks = {1: "",
          2: "",
          3:"",
          4:"",
          5: "",
          6: "",
          7: "",
          8: "",
          9: "",
          }
packages = data[0:8]
instructions = data[10:]

print(packages)

for i in range(8):
    for j in range(1,10):
        if packages[7-i][j*4-3] != " ":
            stacks[j] += packages[7-i][j*4-3]

print(stacks)
for i in instructions:
    temp = i.split()
    #amount of moves 2, 4, 6
    crates = stacks[int(temp[3])][-1*int(temp[1]):]
    stacks[int(temp[3])] = stacks[int(temp[3])][:-1*int(temp[1])]
    stacks[int(temp[5])] += crates

last_sting = ""
for i in range(1, 10):
    last_sting += stacks[i][-1]

print(last_sting)
