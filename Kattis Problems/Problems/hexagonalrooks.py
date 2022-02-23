def convert(point):
    x = point[0]; y = point[1:]
    if ord(x) <= ord('f'):
        return [ord(x) - ord('a'), int(y) - 1]
    else:
        return [ord(x) - ord('a'), int(y) - 1 + ord(x) - ord('f')]

def reach(start,point):
    if start[0] == point[0]:
        return True
    if start[1] == point[1]:
        return True
    if start[1] - start[0] == point[1] - point[0]:
        return True

start,end = input().split()
s = convert(start)
e = convert(end)

count = 0
for row in range(11):
    for col in range(11):
        if max(0,row - 5) <= col < max(0,row - 5) + (11 - abs(5 - row)):
            point = [col, row]
            if point == s or point == e:
                continue
            if reach(s,point) and reach(e, point):
                count += 1
print(count)