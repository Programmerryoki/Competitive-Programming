a,d = map(int, input().split())
ph = [[int(i) for i in input().split()] for j in range(a)]
nh = [[int(i) for i in input().split()] for j in range(d)]
td = sum([i[0] for i in ph])
p = 0; n = td; pt = 0; pn = 0
while p < td:
