A,V  =[int(i) for i in input().split()]
B,W = [int(i) for i in input().split()]
T = int(input())
if V > W:
    if abs(A - B) / abs(V - W) <= T:
        print("YES")
    else:
        print("NO")
else:
    if V == W and A == B:
        print("YES")
    else:
        print("NO")