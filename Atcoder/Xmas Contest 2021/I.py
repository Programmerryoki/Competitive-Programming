A,B,C,D = [int(i) for i in input().split()]
rab = [[A,B],[C,D]]
dis = lambda x,y: abs(x[0]-y[0]) + abs(x[1]-y[1])
while True:
    e,f = [int(i) for i in input().split()]
    if e == 0 and f == 0:
        break
    if dis(rab[0], [e,f]) <= dis(rab[1], [e,f]):
        print(1, flush=True)
        rab[0] = [e,f]
    else:
        print(2, flush=True)
        rab[1] = [e,f]