A,B = [int(i) for i in input().split()]
if A > 0 and B == 0:
    print("Gold")
elif A == 0 and 0 < B:
    print("Silver")
else:
    print("Alloy")