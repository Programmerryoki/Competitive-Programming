N, T = [int(i) for i in input().split()]
A,B,C,t = [int(i) for i in input().split()]
p = [t]
for a in range(N-1):
    p.append((A*p[-1] + B)%C + 1)
p.sort()

tt = 0
ct = 0
i = 0
while i < N and p[i] <= T:
    if T >= p[i]:
        T -= p[i]
        ct += p[i]
        tt += ct
        t = ((A*t + B)%C) + 1
        # print(t)
        i += 1
    else:
        break
print(i, tt%(1000000007))