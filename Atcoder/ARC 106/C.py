N,M = map(int, input().split())
if N == 1:
    print(-1) if M != 0 else print(1,2)
    exit()
if M < 0 or M >= N - 1:
    print(-1)
    exit()

ans = []
lim = N - M - 1
for i in range(1,lim+1):
    ans.append([i, 2*N - i + 1])
for i in range(lim+1, 2*N - lim, 2):
    ans.append([i, i+1])
print("\n".join(" ".join(map(str, i)) for i in ans))