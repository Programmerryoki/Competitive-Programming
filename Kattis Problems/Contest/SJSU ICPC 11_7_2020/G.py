N = int(input())
ans = ""
while N > 0:
    ans += str(N&1)
    N = N >> 1
print(int(ans, 2))