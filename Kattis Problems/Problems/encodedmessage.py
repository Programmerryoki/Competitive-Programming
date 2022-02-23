num = int(input())
for i in range(num):
    msg = input()
    n = int(len(msg)**0.5)
    encri = []
    for a in range(n):
        encri.append(list(msg[:n]))
        msg = msg[n:]
    ans = ""
    for a in range(n):
        ans += "".join([encri[i][n-a-1] for i in range(n)])
    print(ans)