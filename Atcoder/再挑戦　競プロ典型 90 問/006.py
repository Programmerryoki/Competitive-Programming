N,K = [int(i) for i in input().split()]
S = input()

pos = [[float("inf")]*(N+1) for i in range(26)]
for i in range(len(S)-1, -1, -1):
    for j in range(26):
        if ord(S[i]) - ord("a") == j:
            pos[j][i] = i
        else:
            pos[j][i] = pos[j][i+1]

ans = ""
i = 0
while len(ans) < K:
    for j in range(26):
        if pos[j][i] != float("inf") and len(S) - pos[j][i] >= K - len(ans):
            ans += chr(j + ord("a"))
            i = pos[j][i]
            break
    i += 1
print(ans)