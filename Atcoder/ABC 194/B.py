N = int(input())
ppl = [[int(i) for i in input().split()] for j in range(N)]
mi = float("inf")
for i in range(N):
    for j in range(N):
        if i == j:
            val = ppl[i][0] + ppl[j][1]
        else:
            val = max(ppl[i][0], ppl[j][1])
        mi = min(mi, val)
print(mi)