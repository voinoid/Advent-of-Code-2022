
f = open("input6.txt", "r")
data = f.read()
#print(data)
length = len(data)
#print(length)
i = 0
start = False
hashmap = {}
while i < length-14 and start is not True:
    if data[i] in hashmap:
        i = hashmap[data[i]]
        #not the optimal approach, but easy =P
        hashmap = {}
    else:
        hashmap[data[i]] = i

    if len(hashmap) == 14:
        start = True
    i += 1

print("message marker is: " + str(i))