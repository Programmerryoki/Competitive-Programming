t = int(input())
for _ in range(t):
    seq = set()
    seq.add(0)
    n = int(input())
    for a in range(1,n//2+1):
        c = n//a
        if c != 1:
            seq.add(c)
        else:
            seq.add(1)
            break
    if n > 3:
        seq.add(2)
    seq.add(1)
    seq.add(n)
    print(len(seq))
    print(" ".join(map(str, sorted(list(seq)))))