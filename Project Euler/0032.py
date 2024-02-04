p = set()
w = set("123456789")
for a in range(10,100):
    for b in range(100,1000):
        if len(set(str(a)+str(b))) != 5 or len(str(a)+str(b)+str(a*b)) != 9:
            continue
        ss = set(str(a) + str(b) + str(a * b))
        if '0' in ss:
            continue
        if len(w - ss) > 0:
            continue
        # print(ss, w - ss)
        p.add((a,b,a*b))
for a in range(1,10):
    for b in range(1000,10000):
        if len(set(str(a)+str(b))) != 5 or len(str(a)+str(b)+str(a*b)) != 9:
            continue
        ss = set(str(a)+str(b)+str(a*b))
        if '0' in ss:
            continue
        if len(w - ss) > 0:
            continue
        # print(ss, w - ss)
        p.add((a,b,a*b))
print(p)
print(len(p))
print(sum(set(i[-1] for i in p)))