import math
inp = input()
n = int(inp)
ball = [[0,0] for i in range(n*2)]
ask = 0
phase = 0

while inp != "-1":
    if ask <= n and phase == 0:
        if phase == 0:
            print("?"," ".join([str(i) for i in range(ask+1,ask+n+1)]))
            ask = 0
            phase += 1
        else:
            print("?"," ".join([str(i) for i in range(0,n*2) if i%2==0]))
    else:
        break
    inp = input()
    if inp == "Red":
        for a in range(ask,ask+n):
            ball[a][0] += math.ceil(n/2)/n
    elif inp == "Blue":
        for a in range(ask,ask+n):
            ball[a][1] += math.ceil(n/2)/n
    ask += 1
print(ball)


