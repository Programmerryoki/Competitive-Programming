S,T,X = [int(i) for i in input().split()]
if X < S <= T:
    print("No")
elif S <= T <= X:
    print("No")
elif T <= X < S:
    print("No")
else:
    print("Yes")