A,B = [int(i) for i in input().split()]
print((B+A)//2 if not abs(B-A)&1 else "IMPOSSIBLE")