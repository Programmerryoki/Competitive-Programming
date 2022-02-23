pos = ["North", "East", "South", "West"]
a,b,c = [pos.index(i) for i in input().split()]
if (a + 1) % 4 == b and (c == (a+2)%4 or c == (a-1)%4):
    print("Yes")
elif (a + 2) % 4 == b and c == (a-1)%4:
    print("Yes")
else:
    print("No")