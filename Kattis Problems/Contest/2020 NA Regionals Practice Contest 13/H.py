n = int(input())
for _ in range(n):
    a,b,c,d = map(int, input().split())
    m = max(a,b,c)
    pos = []
    a,b,c = sorted([a,b,c])
    ta,tb,tc,td = a,b,c,d
    ta += d//3 + (d%3>=1)
    tb += d//3 + (d%3>=2)
    tc += d//3
    pos.append(ta**2 + tb**2 + tc**2 + 7*min(ta,tb,tc))
    ta,tb,tc,td = a,b,c,d
    ta,td = ta+min(td, tb-ta), td-min(td, tb-ta)
    ta,tb,td = ta+min(td//2, tc-ta),tb+min(td//2,tc-tb),td-min(td//2, tc-ta)
    pos.append(ta**2 + tb**2 + tc**2 + 7*min(ta,tb,tc))
    ta,tb,tc,td = a,b,c,d
    ta += td
    pos.append(ta**2 + tb**2 + tc**2 + 7*min(ta,tb,tc))
    ta,tb,tc,td = a,b,c,d
    tb += td
    pos.append(ta**2 + tb**2 + tc**2 + 7*min(ta,tb,tc))
    ta,tb,tc,td = a,b,c,d
    tc += td
    pos.append(ta**2 + tb**2 + tc**2 + 7*min(ta,tb,tc))
    print(max(pos))
    # if m*3 - (a+b+c) <= d:
    #     a += d//3 + (d%3>=1)
    #     b += d//3 + (d%3>=2)
    #     c += d//3
    # else:
    #     a,d = a+min(d, b-a), d-min(d, b-a)
    #     a,b,d = a+min(d//2, c-a),b+min(d//2,c-b),d-min(d//2, c-a)
    # print(a**2 + b**2 + c**2 + 7*min(a,b,c))