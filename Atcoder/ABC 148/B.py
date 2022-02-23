n = int(input())
s, t = input().split()
ans = []
for a in range(len(s) + len(t)):
    if a%2==0:
        ans.append(s[a//2])
    else:
        ans.append(t[a//2])
print("".join(ans))