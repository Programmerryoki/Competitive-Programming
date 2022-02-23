A,B = [int(i) for i in input().split()]
if B > A:
    print(B - 2)
else:
    print(2*10**9 - B - 1)