from math import ceil
a,b,c = int(input()), int(input()), int(input())
if ceil(a/b) * 2 / 3 >= ceil(a/c):
    print("YES")
else:
    print("NO")