N,W = [int(i) for i in input().split()]
cheeze = [[int(i) for i in input().split()] for _ in range(N)]
cheeze.sort(key=lambda x: (x[0]), reverse=True)
t = 0
w = 0
i = 0
while True:
    if i < len(cheeze) and w + cheeze[i][1] < W:
        w += cheeze[i][1]
        t += cheeze[i][0] * cheeze[i][1]
    elif i < len(cheeze):
        t += cheeze[i][0] * (W - w)
        break
    else:
        break
    i += 1
print(t)