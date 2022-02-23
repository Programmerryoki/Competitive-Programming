n,p,k = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
t.insert(0,0)
t.append(k)
tt = 0
for a in range(len(t) - 1):
    tt += (t[a+1] - t[a]) * (1 + p * a / 100)
print(tt)