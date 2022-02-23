while True:
    line = input()
    if line == "0":
        break
    k,m = map(int, line.split())
    course = [int(i) for i in input().split()]
    cs = set(course)
    mc = True
    for _ in range(m):
        c,r,*cate = [int(i) for i in input().split()]
        # print(cate)
        # print(set(cate) & cs)
        if r > len(set(cate) & cs):
            mc = False
    print("yes" if mc else "no")