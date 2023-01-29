
f = open("input6.txt", "r")
data = f.read()
print(data)
length = len(data)
print(length)
i = 0
start = False
while i < length-4 and start is not True:
    if not (data[i] in data[i+1:i+4] or data[i+1] in data[i+2:i+4] or data[i+2] in data[i+3]):
        start = True
    #print(data[i] +" in "+ data[i+1:i+4])
    else:
        i += 1

print("marker is: " + str(i+4))