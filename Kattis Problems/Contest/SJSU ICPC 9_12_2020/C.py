moves = input()
ball = [1,0,0]
for m in moves:
    if m == "A":
        ball[0], ball[1] = ball[1], ball[0]
    elif m == "B":
        ball[1],ball[2] = ball[2], ball[1]
    else:
        ball[0],ball[2] = ball[2], ball[0]
print(ball.index(1) + 1)