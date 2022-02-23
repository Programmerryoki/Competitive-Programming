t = int(input())
for a in range(t):
    n = int(input())
    package = []
    for b in range(n):
        package.append([int(i) for i in input().split()])
    package.sort()

    path = ""
    x = 0
    y = 0
    for i in package:
        # print(i)
        if i[0] < x or i[1] < y:
            print("NO")
            break
        else:
            path = path + "R"*(i[0]-x)
            path = path + "U"*(i[1]-y)
            x = i[0]
            y = i[1]
        # print(path)
    else:
        print("YES")
        print(path)