T = int(input())
for _ in range(T):
    n = int(input())
    nv = [int(input()) for i in range(n)]
    s = sum(nv)
    m = max(nv)
    if nv.count(m) != 1:
        print("no winner")
        continue
    print(("majority" if m > s//2 else "minority"),"winner",nv.index(m)+1)