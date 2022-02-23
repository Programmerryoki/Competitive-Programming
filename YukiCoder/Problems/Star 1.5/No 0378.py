N = int(input())
ans = [N]
while N != 0:
    N = N//2
    ans.append(N)
s = t = sum(ans)
m = 0
for i in ans:
    if i*2 > s:
        m = max(m, i*2 - s)
    s -= i
print(m)