N = int(input())
S = input()
if S[0] != S[-1]:
    print(1)
    exit()
for i in range(N-2, 0, -1):
    if S[i] != S[0] and S[i+1] != S[0]:
        print(2)
        exit()
print(-1)