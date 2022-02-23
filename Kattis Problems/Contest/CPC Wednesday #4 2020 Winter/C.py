m = int(input())
for a in range(m):
    X,Y = map(float, input().split())
    n = int(input())
    pos = False
    for b in range(n):
        x,y = map(float, input().split())
        if ((X-x)**2 + (Y-y)**2)**0.5 <= 8:
            pos = True
    if pos:
        print("light a candle")
    else:
        print("curse the darkness")