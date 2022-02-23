N = int(input())
S = [int(input()) for _ in range(N)]
m = 0
score = sum(S)
if score%10 != 0:
    print(score)
    exit()

for s in S:
    if (score - s) % 10 != 0:
        m = max(m, score - s)
print(m)