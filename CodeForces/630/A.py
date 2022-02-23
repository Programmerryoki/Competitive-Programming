t = int(input())
for _ in range(t):
    a,b,c,d = [int(i) for i in input().split()]
    x,y,x1,y1,x2,y2 = [int(i) for i in input().split()]
    if x1 <= x + a - b <= x2 and y1 <= y + c - d <= y2:
        if (a <= x-x1 or b <= x-x1 or a <= x2-x or b <= x2-x) and (c <= y-y1 or d <= y-y1 or c <= y2-y or d <= y2-y):
            print("YES")
        else:
            print("NO")
    elif x1 <= x + b - a <= x2 and y1 <= y + d - c <= y2:
        if (a <= x-x1 or b <= x-x1 or a <= x2-x or b <= x2-x) and (c <= y-y1 or d <= y-y1 or c <= y2-y or d <= y2-y):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")