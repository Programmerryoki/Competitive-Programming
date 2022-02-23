n = int(input())
grid = [input() for i in range(n)]
for i in grid:
    if i.count("W") != len(i) // 2:
        print(0)
        exit()
    if "WWW" in i or "BBB" in i:
        print(0)
        exit()
for i in range(n):
    arr = [grid[j][i] for j in range(n)]
    if arr.count("W") != len(arr) // 2:
        print(0)
        exit()
    string = "".join(arr)
    if "WWW" in string or "BBB" in string:
        print(0)
        exit()
print(1)