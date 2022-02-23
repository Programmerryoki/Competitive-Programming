N,M = map(int, input().split())
koma = {}
for _ in range(M):
    X,Y = [int(i) for i in input().split()]
    if X in koma:
        koma[X].add(Y)
    else:
        koma[X] = {Y}
order = list(koma.keys())
order.sort()
pos = {N}
for o in order:
    check = koma[o]
    new = set()
    for c in check:
        if c-1 in pos:
            new.add(c)
        elif c+1 in pos:
            new.add(c)
    pos -= check
    pos |= new
# print(pos)
print(len(pos))