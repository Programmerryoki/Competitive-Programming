N = int(input())
pos = [0,0]
time = 0
for _ in range(N):
    t,x,y = [int(i) for i in input().split()]
    d = abs(pos[0] - x) + abs(pos[1] - y)
    if d > t - time:
        print("No")
        break
    elif (t - time - d)%2 != 0:
        print("No")
        break
    pos = [x,y]
    time = t
else:
    print("Yes")