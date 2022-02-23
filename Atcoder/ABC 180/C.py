N = int(input())
ans = []
bans = []
for i in range(1,int(N**0.5) + 1):
    if N%i == 0:
        ans.append(i)
        if i != N//i:
            bans.append(N//i)
print("\n".join(map(str, ans)))
print("\n".join(map(str, bans[::-1])))