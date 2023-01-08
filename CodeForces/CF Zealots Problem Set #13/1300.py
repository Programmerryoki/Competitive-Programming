t = int(input())
for _ in range(t):
    W,H = [int(i) for i in input().split()]
    x1,y1,x2,y2 = [int(i) for i in input().split()]
    w,h = [int(i) for i in input().split()]

    cases = [
        (W < w + (x2-x1)) and (h + (y2-y1) > H),
        (H < h + (y2-y1)) and (w + (x2-x1) > W),
    ]
    if any(cases):
        print(-1)
        continue
    dis = 0
    if w + (x2 - x1) <= W and h + (y2 - y1) <= H:
        dis = min([max(0,w-x1),max(0,w-(W-x2)),max(0,h-y1),max(0,h-(H-y2))])
    elif w + (x2 - x1) <= W:
        dis = min(max(0,w-x1), max(0,w-(W-x2)))
    elif h + (y2 - y1) <= H:
        dis = min(max(0,h-y1), max(0,h-(H-y2)))
    print(dis)