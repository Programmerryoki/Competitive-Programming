r, c = [int(i) for i in input().split()]
maps = [input() for i in range(r)]
seen = set()


def search(a,b):
    seen.add(str(a)+","+str(b))
    if 0 <= a - 1 and (maps[a-1][b] == "L" or maps[a-1][b] == "C") and (str(a-1) + "," + str(b) not in seen):
        search(a-1,b)
    if a + 1 < r and (maps[a+1][b] == "L" or maps[a+1][b] == "C") and (str(a+1) + "," + str(b) not in seen):
        search(a+1,b)
    if 0 <= b - 1 and (maps[a][b-1] == "L" or maps[a][b-1] == "C") and (str(a) + "," + str(b-1) not in seen):
        search(a,b-1)
    if b+1 < c and (maps[a][b+1] == "L" or maps[a][b+1] == "C") and (str(a) + "," + str(b+1) not in seen):
        search(a,b+1)


Noland = 0
for a in range(r):
    for b in range(c):
        if maps[a][b] == "L" and (str(a) + "," + str(b) not in seen):
            Noland += 1
            search(a,b)
# print(seen)
print(Noland)