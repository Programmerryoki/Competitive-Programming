t = int(input())
for _ in range(t):
    n = int(input())
    rows = [input() for i in range(2)]
    for i in range(n):
        if rows[0][i] == "1" and rows[1][i] == "1":
            print("NO")
            break
    else:
        print("YES")