A, B, C = [int(i) for i in input().split()]
if A < B:
    if (A+C) / 2 > B:
        if (C-A)&1:
            print((A+C+1)//2 - B + 1)
        else:
            print((A+C)//2 - B)
    else:
        print(B + (B - A) - C)
elif A == B:
    if (A+C) / 2 > B:
        if (C-A)&1:
            print((A+C+1)//2 - B + 1)
        else:
            print((A+C)//2 - B)
    else:
        print(B - C)
else:
    if (A+C) / 2 > B:
        if (C-A)&1:
            print((A+C+1)//2 - B + 1)
        else:
            print((A+C)//2 - B)
    else:
        print(B - (A - B) - C)