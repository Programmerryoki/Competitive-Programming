t = int(input())
for _ in range(t):
    a,b = [int(i) for i in input().split()]
    a,b = max(a,b), min(a,b)
    sho = min(a//2, b)
    a -= sho*2
    b -= sho
    sw = 0
    p = sho + sw
    while sho + sw > p:
        p = sho + sw
        sho -= 1
        a += 2
        b += 1
        sw = min(a, b//2)
    print(sho + sw)