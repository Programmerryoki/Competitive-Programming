x1,y1,x2,y2 = map(int, input().split())
move = [x2 - x1, y2 - y1]
x3, y3 = x2 - move[1], y2 + move[0]
x4, y4 = x3 - move[0], y3 - move[1]
print(x3, y3, x4, y4)