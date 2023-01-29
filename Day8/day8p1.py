f = open("input8.txt", "r")
data = f.readlines()
data = [line.replace('\n', '') for line in data]
# print(data)
visible_trees = 2*len(data) + 2*len(data[0]) - 4
print(visible_trees)
hash_visible_trees = {}
row_len = len(data[0])
col_len = len(data)
#print(row_len)
#print(col_len)

# check for visible from left
for r, row in enumerate(data[1:-1], start=1):
    highest_left = int(row[0])
    for t, tree in enumerate(row[1:-1], start=1):
        if int(tree) > highest_left:
            # map at row:column
            hash_visible_trees[str(r) + "_" + str(t)] = ""
            highest_left = int(tree)

print(len(hash_visible_trees))
#print(hash_visible_trees)
# check for visible from right
for r, row in enumerate(data[1:-1], start=1):
    highest_right = int(row[-1])
    row = row[::-1]
    for t, tree in enumerate(row[1:-1], start=1):
        if int(tree) > highest_right:
            # map at row:column
            if (str(r) + "_" + str(row_len - t)) not in hash_visible_trees:
                hash_visible_trees[str(r) + "_" + str(row_len - t)] = ""
            highest_right = int(tree)
print(len(hash_visible_trees))
#print(hash_visible_trees)
# check for visible from top
for col in range(1, row_len-1):
    highest_top = int(data[0][col])
    #print(highest_top)
    for r, row in enumerate(data[1:-1], start=1):
        #print(row[col])
        tree = row[col]
        if int(tree) > highest_top:
            # map at row:column
            #print(str(highest_top) + " " + tree)
            if (str(r) + "_" + str(col)) not in hash_visible_trees:
                hash_visible_trees[str(r) + "_" + str(col)] = ""
            #print(str(r) + "_" + str(col))
            highest_top = int(tree)

print(len(hash_visible_trees))
# print(hash_visible_trees)
# check for visible from bottom
data.reverse()
for col in range(1, row_len-1):
    highest_bot = int(data[0][col])
    #print(highest_top)
    for r, row in enumerate(data[1:-1], start=1):
        #print(row[col])
        tree = row[col]
        if int(tree) > highest_bot:
            # map at row:column
            #print(str(highest_top) + " " + tree)
            if (str(row_len - r - 1) + "_" + str(col)) not in hash_visible_trees:
                hash_visible_trees[str(row_len - r - 1) + "_" + str(col)] = ""
            #print(str(r) + "_" + str(col))
            highest_bot = int(tree)
# for col in range(1, row_len-1):
#     highest_bot = int(data[col_len-1][col])
#     print(highest_bot)
#     data.reverse()
#     for r, row in enumerate(data[1:-1], start=1):
#         tree = row[col]
#         if int(tree) > highest_bot:
#             # map at row:column
#             if (str(row_len - r - 1) + "_" + str(col)) not in hash_visible_trees:
#                 hash_visible_trees[str(row_len - r - 1) + "_" + str(col)] = ""
#                 #print(tree)
#             highest_bot = int(tree)
print(len(hash_visible_trees))
visible_trees += len(hash_visible_trees)
print(visible_trees)
print(hash_visible_trees)
