N,M = [int(i) for i in input().split()]
S = input().split()
T = input().split()
ST = set(T)
ans = ["No"] * N
for i in range(len(S)):
    if S[i] in ST:
        ans[i] = "Yes"
print("\n".join(ans))