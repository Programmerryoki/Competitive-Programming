N = int(input())
tc = 0
tw = 0
for _ in range(N):
    t, s = input().split()
    t = int(t)
    tc += min((12*t)//1000, len(s))
    tw += max(len(s) - (12*t)//1000, 0)
print(tc, tw)