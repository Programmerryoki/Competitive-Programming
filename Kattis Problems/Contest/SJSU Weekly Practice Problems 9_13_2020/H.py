while True:
    nx,ny,w = [float(i) for i in input().split()]
    if nx == ny == w == 0:
        break
    w /= 2
    x = [float(i) for i in input().split()]
    y = [float(i) for i in input().split()]
    x.sort(); y.sort()

    cutx = [[0,75]]
    for cut in x:
        cl, ch = cut - w, cut + w
        nx = []
        for xi,yi in cutx:
            if cl <= xi < yi <= ch:
                continue
            if cl <= xi <= ch < yi:
                nx.append([ch, yi])
            if xi < cl <= yi <= ch:
                nx.append([xi, cl])
            if xi < cl <= ch < yi:
                nx.append([xi, cl])
                nx.append([ch, yi])
            if ch < xi or cl > yi:
                nx.append([xi,yi])
        cutx = nx
        # print(cutx)

    cuty = [[0,100]]
    for cut in y:
        cl, ch = cut - w, cut + w
        ny = []
        for xi,yi in cuty:
            if cl <= xi < yi <= ch:
                continue
            if cl <= xi <= ch < yi:
                ny.append([ch, yi])
            if xi < cl <= yi <= ch:
                ny.append([xi, cl])
            if xi < cl <= ch < yi:
                ny.append([xi, cl])
                ny.append([ch, yi])
            if ch < xi or cl > yi:
                ny.append([xi,yi])
        cuty = ny
        # print(cuty)

    print("YES" if len(cuty) == 0 and len(cutx) == 0 else "NO")