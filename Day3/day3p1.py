def getPriorityNumber(char):
    num = ord(char) - 96
    if num > 0: return num
    return num + 58

f = open("input3.txt", "r")
data = f.readlines()
priority_count = 0

for item in data:
    item = item.rstrip()
    n = len(item)//2
    half1 = item[0:n]
    half2 = item[n:]
    char = "".join(set(half1).intersection(half2))
    priority_count += getPriorityNumber(char)
    #ord(char) a-z is 97-122; A-Z is 65-90

#print(data)
print(priority_count)


