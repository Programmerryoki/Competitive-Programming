N = int(input())
S = input()
m = 0
for i in range(1,N):
    m = max(m, len(set(S[:i]) & set(S[i:])))
print(m)