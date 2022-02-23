p,q = [int(i) for i in input().split()]
if p&1 and q&1:
    print(1)
elif not p&1:
    print(0)
elif p < q:
    print(2)
else:
    print(0)