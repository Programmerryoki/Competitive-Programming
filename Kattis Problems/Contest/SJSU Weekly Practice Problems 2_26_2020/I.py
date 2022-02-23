N, M = [int(i) for i in input().split()]
inter = [[1]]
for _ in range(M):
    a,b = [int(i) for i in input().split()]
    connect = []
    for i, o in enumerate(inter):
        A = a in o
        B = b in o
        if A and B:
            connect.append(i)
        elif A:
            connect.append(i)
            inter[i].append(b)
        elif B:
            connect.append(i)
            inter[i].append(a)

    if len(connect) == 0:
        inter.append([a,b])
    else:
        ini = connect[0]
        for i in (connect[1:])[::-1]:
            inter[ini] += inter.pop(i)

    # print(inter)

if len(inter[0]) == N:
    print("Connected")
else:
    notconnect = [i for i in range(1,N+1) if i not in inter[0]]
    print("\n".join(map(str, notconnect)))