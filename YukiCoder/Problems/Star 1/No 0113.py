S = input()
x,y = 0,0
for s in S:
    x += s == "N"
    x -= s == "S"
    y += s == "E"
    y -= s == "W"
print((x**2 + y**2)**0.5)