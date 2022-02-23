pos = [set() for i in range(10)]
S = input()
for i,s in enumerate(S):
    pos[int(s)].add(i)
n = "2019"
no = 0
while len(n) < len(S):
    P = pos[int(n[0])]
    for d in n[1:]:
        t = set()
        for p in P:
            if p+1 in pos[int(d)]:
                t.add(p+1)
        P = t
        if len(P) == 0:
            break
    else:
        no += len(P)
    n = str(int(n)+2019)
print(no)