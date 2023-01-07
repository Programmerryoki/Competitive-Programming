N = int(input())
pos = [0,0]
ct = 0
for t,x,y in [[int(i) for i in input().split()] for _ in range(N)]:
    d = abs(pos[0]-x) + abs(pos[1]-y)
    if d > t - ct or (d - t - ct) & 1:
        print("No")
        break
    ct = t
    pos = [x,y]
else:
    print("Yes")