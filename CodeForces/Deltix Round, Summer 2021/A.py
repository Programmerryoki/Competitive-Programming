t = int(input())
for _ in range(t):
    c,d = [int(i) for i in input().split()]
    mid = (c + d) / 2
    if mid.is_integer():
        if c == mid and c == 0:
            print(0)
        elif c == mid:
            print(1)
        else:
            print(2)
    else:
        print(-1)