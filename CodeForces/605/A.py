q = int(input())
for _ in range(q):
    a,b,c = [int(i) for i in input().split()]
    t = abs(a-b)+abs(a-c)+abs(b-c)
    if t-4 < 0:
        t = 0
    else:
        t -= 4
    print(t)