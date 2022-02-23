from itertools import combinations_with_replacement

a,_,b,_,c = input().split()
print(a,b,c)
la = len(a); qa = a.count("?")
lb = len(b); qb = b.count("?")
lc = len(c); qc = c.count("?")
tqn = qa+qb+qc
tn = 0
for comb in combinations_with_replacement([str(i) for i in range(1,10)], tqn):
    ta = ""
    j = 0
    for i in a:
        if i == "?":
            ta += comb[j]
            j += 1
        else:
            ta += i
    if len(str(int(ta))) != la:
        continue

    tb = ""
    for i in b:
        if i == "?":
            tb += comb[j]
            j += 1
        else:
            tb += i
    if len(str(int(tb))) != lb:
        continue

    tc = ""
    for i in c:
        if i == "?":
            tc += comb[j]
            j += 1
        else:
            tc += i
    if len(str(int(tc))) != lc:
        continue

    print(ta, tb, tc, int(ta) ^ int(tb))
    if int(ta) ^ int(tb) == int(tc):
        tn += 1
print(tn)