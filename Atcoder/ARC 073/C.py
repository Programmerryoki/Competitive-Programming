N,T = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
pt = 0
tt = 0
for i in range(N):
    tt += min(T, t[i] - pt)
    pt = t[i]
print(tt + T)