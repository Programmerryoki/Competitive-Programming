N = int(input())
S = input()
T = list(input())
count = 0
rev = {"A":"B","B":"A"}
for i in range(N):
    if S[i] == T[i]:
        continue
    count += 1
    T[i], T[i+1] = rev[T[i]], rev[T[i+1]]
print(count if T[-1] == S[-1] else -1)