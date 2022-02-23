import bisect

n = int(input())
robot = []
for a in range(n):
    x, l = [int(i) for i in input().split()]
    index = bisect.bisect_left(robot, [x,l])
    valid = True
    i = index
    if len(robot) == 0:
        robot.append([x,l])
        continue

    while len(robot) > i >= 0 and robot[i][0] + robot[i][1] > x-l:
        t = robot[i]
        if x-l < t[0]-t[1] < x+l:
            valid = False
            break
        elif x-l < t[0]+t[1] < x+l:
            valid = False
            break
        i -= 1

    i = index
    while i < len(robot) and robot[i][0] - robot[i][1] < x+l:
        t = robot[i]
        if x-l < t[0]-t[1] < x+l:
            valid = False
            break
        elif x-l < t[0]+t[1] < x+l:
            valid = False
            break
        i += 1

    if valid:
        robot.insert(index, [x,l])
print(robot)
print(len(robot))

# n = int(input())
# robot = []
# for a in range(n):
#     x,l = [int(i) for i in input().split()]
#     remove = []
#     add = []
#     for i in robot:
#         if x-l < i[0]-i[1] < x+l or x-l < i[0] < x+l or x-l < i[0]+i[1] < x+l:
#             if i[1] > l:
#                 remove.append(i)
#             break
#         else:
#             continue
#     else:
#         robot.append([x,l])
# print(len(robot))