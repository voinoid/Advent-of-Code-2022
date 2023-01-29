def getPriorityNumber(char):
    num = ord(char) - 96
    if num > 0: return num
    return num + 58

f = open("input3.txt", "r")
data = f.readlines()
priority_count = 0

for i in range(len(data)//3):
    pack1 = set(data[i*3].rstrip())
    pack2 = set(data[i*3+1].rstrip())
    pack3 = set(data[i*3+2].rstrip())
    char = "".join(set.intersection(pack1, pack2, pack3))
    #char = "".join(set.intersection(pack1, pack2, pack3))
    print(char)
    priority_count += getPriorityNumber(char)
    #ord(char) a-z is 97-122; A-Z is 65-90

#print(data)
print(priority_count)


