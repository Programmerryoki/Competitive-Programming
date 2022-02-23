n = int(input())
move = input()
vis = [0]*n
i = 0
cur = move[0]
while i < n-1:
    try:
        if cur == "R":
            j = move.index("L", i)
        else:
            j = move.index("R", i)
    except:
        j = n-1
    if j < n-1:
        cur = move[j]
        print(j, cur, j - i)
    i = j
# 2
# 2 3
# 1
# 3
# 10
# 2 5
# 1
# 3
# 4
# 7
# 8
