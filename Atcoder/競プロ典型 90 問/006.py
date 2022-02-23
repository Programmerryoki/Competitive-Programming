N,K = [int(i) for i in input().split()]
S = input()
sm = [[float("inf")]*(len(S)+1) for i in range(26)]
for i in range(len(S)-1, -1, -1):
    for j in range(26):
        if ord(S[i]) - ord('a') == j:
            sm[j][i] = i
        else:
            sm[j][i] = sm[j][i+1]
# for i in sm:
#     print(i)
ans = ""
ind = 0
while len(ans) < K:
    for i in range(26):
        if sm[i][ind] == float("inf") or len(S) - sm[i][ind] < K - len(ans):
            continue
        ans += chr(i + ord("a"))
        ind = sm[i][ind]+1
        break
    # print(ans, ind)
print(ans)