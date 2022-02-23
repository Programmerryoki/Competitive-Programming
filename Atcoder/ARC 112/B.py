B,C = map(int, input().split())
if B == 0:
    print(1 + C//2 + (C-1)//2)
elif abs(B) == 1 and C == 1:
    print(2)
elif B > 0:
    sub = C // 2
    sub1 = (C-1)//2
    sub2 = (C-2)//2
    total = 2
    if B - sub <= 0:
        total += B
    else:
        total += sub
    total += sub1
    if -B + sub1 >= 0:
        total += B-1
    else:
        total += sub1
    total += sub2
    print(total)
else:
    sub = C // 2
    sub1 = (C-1)//2
    sub2 = (C-2)//2
    total = 2
    total += sub
    total += sub1
    if -B - sub1 <= 0:
        total += -B
    else:
        total += sub1
    if B + sub2 >= 0:
        total += -B-1
    else:
        total += sub2
    print(total)