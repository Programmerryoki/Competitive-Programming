x,y = map(int, input().split())
if x == 2 and y == 2:
    print("Yes")
elif x in [4,6,9,11] and y in [4,6,9,11]:
    print("Yes")
elif x in [1,3,5,7,8,10,12] and y in [1,3,5,7,8,10,12]:
    print("Yes")
else:
    print("No")