X,Y = map(int, input().split())
if Y == 1 and X == 0:
    print("ALL GOOD")
    exit()
try:
    print(X / (1 - Y))
except:
    print("IMPOSSIBLE")