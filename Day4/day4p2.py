
f = open("input4.txt", "r")
data = f.readlines()
count = 0

for item in data:
    item = item.rstrip()
    p1 = item.split(",")[0].split("-")
    p2 = item.split(",")[1].split("-")
    p1small = int(p1[0])
    p1large = int(p1[1])
    p2small = int(p2[0])
    p2large = int(p2[1])
    if (p1small <= p2small and p1large >=p2small) \
            or (p1small <= p2large and p1large >=p2large)\
            or (p1small >= p2small and p1large <=p2large): count += 1

print(count)


