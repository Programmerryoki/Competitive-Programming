N = int(input())
ts = 0
for _ in range(N):
    s, w = input().split()
    s = [int(i) for i in s.split(":")]
    w = [int(i) for i in w.split(":")]
    if s > w:
        s[0] = s[0] - 24 if s[1] == 0 else s[0] - 23
        s[1] = s[1] - 60 if s[1] != 0 else 0
    ts += (w[0] - s[0])*60 + (w[1] - s[1])
print(ts)